using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private readonly UserService _userService;

        public UsersController(UserService userService)
        {
            _userService = userService;
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

        [HttpPost]
        public ActionResult<User> Create(User user)
        {
            Regex regexEmail = new Regex(@"^[\w!#$%&'*+\-/=?\^_`{|}~]+(\.[\w!#$%&'*+\-/=?\^_`{|}~]+)*" + "@" + @"((([\-\w]+\.)+[a-zA-Z]{2,4})|(([0-9]{1,3}\.){3}[0-9]{1,3}))$");
            Match matchEmail = regexEmail.Match(user.Email);

            Regex regexPassword = new Regex(@"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$");
            Match matchPassword = regexPassword.Match(user.Password);

            //password must have a minimum of 8 characters, at least one number and one letter

            var usernameExists = _userService.GetByName(user.Username);
            var emailExists = _userService.GetByEmail(user.Email);
            var newUsernameLength = user.Username.Length;

            if (usernameExists == null && emailExists == null
                && matchEmail.Success && newUsernameLength >= 3 && matchPassword.Success)
            {
                _userService.Create(user);
            }
            else
            {
                return NoContent();
            }

            return CreatedAtRoute("GetUser", new { id = user.Id.ToString() }, user);
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