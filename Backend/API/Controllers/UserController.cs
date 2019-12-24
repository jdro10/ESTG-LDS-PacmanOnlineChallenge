using API.Models;
using API.Services;
using API.Helpers;
using API.Dtos;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.Extensions.Options;
using Microsoft.AspNetCore.Authorization;
using System.Text;
using System;
using Microsoft.IdentityModel.Tokens;
using System.Security.Claims;
using System.Security.Cryptography;

namespace API.Controllers
{
    [Authorize]
    [Route("api/user")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private readonly UserService _userService;
        private readonly DailyChallengeService _dailyChallengeService;
        private readonly EmailService _emailService;
        private readonly AppSettings _appSettings;
        private readonly RankService _rankService;

        public UsersController(UserService userService, IOptions<AppSettings> appSettings, DailyChallengeService dailyChallengeService, EmailService emailService, RankService rankService)
        {
            _userService = userService;
            _appSettings = appSettings.Value;
            _dailyChallengeService = dailyChallengeService;
            _emailService = emailService;
            _rankService = rankService;
        }

        [AllowAnonymous]
        [HttpPost("auth")]
        public IActionResult Authenticate([FromBody]UserDto userInfo)
        {
            var user = _userService.Authenticate(userInfo.Username);

            if (user == null || !(VerifyPasswordHash(userInfo.Password, user.PasswordHash, user.PasswordSalt)))
            {
                return BadRequest(new { error = "Username ou password incorreta!" });
            }

            var tokenHandler = new JwtSecurityTokenHandler();
            var key = Encoding.ASCII.GetBytes(_appSettings.Secret);
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(new Claim[]
                {
                    new Claim(ClaimTypes.Name, user.Id.ToString())
                }),
                Expires = DateTime.UtcNow.AddDays(7),
                SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
            };

            var token = tokenHandler.CreateToken(tokenDescriptor);
            var tokenString = tokenHandler.WriteToken(token);

            SetUserChallengeDaily(user);

            return Ok(new
            {
                Id = user.Id,
                Username = user.Username,
                Email = user.Email,
                Token = tokenString,
                Level = user.Level,
                Challenges = user.dailyChallenges
            });
        }

        private void SetUserChallengeDaily(User user)
        {
            DateTime dt = DateTime.Now;
            var challenges = _dailyChallengeService.GetByDay(((int)dt.DayOfWeek).ToString());

            user.dailyChallenges = challenges;
            
            _userService.Update(user.Id, user);
        }

        [HttpGet]
        public ActionResult<List<User>> Get() =>
            _userService.Get();

        [HttpGet("{id:length(24)}", Name = "GetUser")]
        public ActionResult<User> Get(string id)
        {
            var user = _userService.Get(id);

            if (user == null)
            {
                return NotFound();
            }

            return user;
        }

        [AllowAnonymous]
        [HttpPost]
        public ActionResult<User> Create(User user)
        {
            Regex regexEmail = new Regex(@"^[\w!#$%&'*+\-/=?\^_`{|}~]+(\.[\w!#$%&'*+\-/=?\^_`{|}~]+)*" + "@" + @"((([\-\w]+\.)+[a-zA-Z]{2,4})|(([0-9]{1,3}\.){3}[0-9]{1,3}))$");
            Match matchEmail = regexEmail.Match(user.Email);

            Regex regexPassword = new Regex(@"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$");
            Match matchPassword = regexPassword.Match(user.Password);

            byte[] passwordHash, passwordSalt;
            CreatePasswordHash(user.Password, out passwordHash, out passwordSalt);

            var usernameExists = _userService.GetByName(user.Username);
            var emailExists = _userService.GetByEmail(user.Email);
            var newUsernameLength = user.Username.Length;

            if (usernameExists == null && emailExists == null
                && matchEmail.Success && newUsernameLength >= 3 && matchPassword.Success)
            {
                user.PasswordHash = passwordHash;
                user.PasswordSalt = passwordSalt;
                user.Level = 0;
                user.Score = 0;
                //_emailService.sendSignupMail(user.Email, user.Username, user.Password);
                _userService.Create(user);
            }
            else
            {
                return Ok(new
                {
                    success = "false",
                    error = "Username/email já existente ou password inválida"
                });
            }

            return Ok(new
            {
                success = "true",
                error = ""
            });
        }

        private static void CreatePasswordHash(string password, out byte[] passwordHash, out byte[] passwordSalt)
        {
            using (var hmac = new HMACSHA512())
            {
                passwordSalt = hmac.Key;
                passwordHash = hmac.ComputeHash(Encoding.UTF8.GetBytes(password));
            }
        }

        private static bool VerifyPasswordHash(string password, byte[] storedHash, byte[] storedSalt)
        {
            using (var hmac = new System.Security.Cryptography.HMACSHA512(storedSalt))
            {
                var computedHash = hmac.ComputeHash(System.Text.Encoding.UTF8.GetBytes(password));

                for (int i = 0; i < computedHash.Length; i++)
                {
                    if (computedHash[i] != storedHash[i]) return false;
                }
            }

            return true;
        }

        [AllowAnonymous]
        [HttpPut("{id:length(24)}")]
        public IActionResult ForgotPassword(string id)
        {
            var user = _userService.Get(id);

            if (user == null)
            {
                return NotFound();
            }

            var newPassword = NewRandomPassword();

            byte[] passwordHash, passwordSalt;
            CreatePasswordHash(newPassword, out passwordHash, out passwordSalt);

            user.Password = newPassword;
            user.PasswordHash = passwordHash;
            user.PasswordSalt = passwordSalt;

            _userService.Update(id, user);

            _emailService.newPasswordRequest(user.Email, user.Username, user.Password);

            return Ok(new
            {
                success = "true",
            });
        }

        private static string NewRandomPassword()
        {
            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[8];
            var random = new Random();

            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }

            var finalString = new String(stringChars);

            return finalString;
        }

        [HttpDelete("{id:length(24)}")]
        public IActionResult Delete(string id)
        {
            var user = _userService.Get(id);

            if (user == null)
            {
                return NotFound();
            }

            _userService.Remove(user.Id);

            return NoContent();
        }
    }
}