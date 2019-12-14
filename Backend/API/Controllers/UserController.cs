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
    [Route("api/[controller]")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private readonly UserService _userService;
        private readonly DailyChallengeService _dailyChallengeService;
        private readonly AppSettings _appSettings;

        public UsersController(UserService userService, IOptions<AppSettings> appSettings, DailyChallengeService dailyChallengeService)
        {
            _userService = userService;
            _appSettings = appSettings.Value;
            _dailyChallengeService = dailyChallengeService;
        }

        [AllowAnonymous]
        [HttpPost("auth")]
        public IActionResult Authenticate([FromBody]UserDto userInfo)
        {
            DateTime dt = DateTime.Now;

            var challenges = _dailyChallengeService.GetByDay(((int) dt.DayOfWeek).ToString());
            var user = _userService.Authenticate(userInfo.Username);
            LevelController c = new LevelController();
             

            if (user == null || !(VerifyPasswordHash(userInfo.Password, user.PasswordHash, user.PasswordSalt)))
            {
                return BadRequest(new { error = "Username ou password incorreta" });
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
            
            user.dailyChallenges = challenges;
            user.Level = c.setLevel(user);

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
            //password must have a minimum of 8 characters, at least one number and one letter

            byte[] passwordHash, passwordSalt;
            CreatePasswordHash(user.Password, out passwordHash, out passwordSalt);

            var usernameExists = _userService.GetByName(user.Username);
            var emailExists = _userService.GetByEmail(user.Email);
            var newUsernameLength = user.Username.Length;

            DateTime dt = DateTime.Now;

            var challenges = _dailyChallengeService.GetByDay(((int)dt.DayOfWeek).ToString());

            user.dailyChallenges = challenges;

            if (usernameExists == null && emailExists == null
                && matchEmail.Success && newUsernameLength >= 3 && matchPassword.Success)
            {
                user.PasswordHash = passwordHash;
                user.PasswordSalt = passwordSalt;
                user.Level = 0;
                user.Score = 0;
                _userService.Create(user);
            }
            else
            {
                return BadRequest(new
                {
                    success = "false",
                    error = "Username ou email já existente"
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

        [HttpPut("{id:length(24)}")]
        public IActionResult Update(string id, User userIn)
        {
            var user = _userService.Get(id);

            if (user == null)
            {
                return NotFound();
            }

            _userService.Update(id, userIn);

            return NoContent();
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