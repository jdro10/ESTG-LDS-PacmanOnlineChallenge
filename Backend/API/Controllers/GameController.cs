using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using System;
using API.Dtos;

namespace API.Controllers
{
    [Route("api/game")]
    [ApiController]
    public class GameController : ControllerBase
    {
        private UserService _userService;

        public GameController(UserService userService)
        {
            _userService = userService;
        }

        [AllowAnonymous]
        [HttpPost]
        public void Update(UserUpdate up)
        {
            int result = Int32.Parse(up.Score);
            var userToUpdate = _userService.GetByName(up.Username);

            userToUpdate.Score += result;

            _userService.UpdateScore(userToUpdate.Username, userToUpdate);
        }
    }
}