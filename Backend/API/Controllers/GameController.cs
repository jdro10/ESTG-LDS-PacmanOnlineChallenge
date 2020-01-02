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

        [HttpPost("checkchallenge")]
        public IActionResult checkIfPlayerCompletedChallenge(UserUpdate up)
        {
            int result = Int32.Parse(up.Score);
            var userToUpdate = _userService.GetByName(up.Username);

            for (int i = 0; i < userToUpdate.dailyChallenges.Length; i++)
            {
                if (userToUpdate.dailyChallenges[i] != null && userToUpdate.dailyChallenges[i].Points == 500)
                {
                    userToUpdate.todayDoneChallenge[i] = userToUpdate.dailyChallenges[i].Id;
                    userToUpdate.dailyChallenges[i] = null;
                    userToUpdate.Score += 500;
                    _userService.UpdateScore(userToUpdate.Username, userToUpdate);
                }
            }

            if (result >= 1000)
            {
                for (int i = 0; i < userToUpdate.dailyChallenges.Length; i++)
                {
                    if (userToUpdate.dailyChallenges[i] != null && userToUpdate.dailyChallenges[i].Id == userToUpdate.todayDoneChallenge[i])
                    {
                        return NoContent();
                    }
                    else
                    {
                        if (userToUpdate.dailyChallenges[i] != null && userToUpdate.dailyChallenges[i].Points == 750)
                        {
                            userToUpdate.todayDoneChallenge[i] = userToUpdate.dailyChallenges[i].Id;
                            userToUpdate.dailyChallenges[i] = null;
                            userToUpdate.Score += 750;
                            _userService.UpdateScore(userToUpdate.Username, userToUpdate);
                            break;
                        }
                    }
                }                
            }
            return Ok();
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