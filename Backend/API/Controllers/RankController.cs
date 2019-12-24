using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using System;

namespace API.Controllers
{
    [Authorize]
    [Route("api/ranks")]
    [ApiController]
    public class RankController : ControllerBase
    {
        private readonly RankService _rankService;
        private List<User> _userRank;
        private readonly UserService _userService;
        private readonly LevelService _levelService;

        public RankController(RankService rankService, UserService userService, LevelService levelService)
        {
            _rankService = rankService;
            _userRank = new List<User>();
            _userService = userService;
            _levelService = levelService;
        }

        private List<User> OrderByScore()
        {
            var users = _rankService.GetAllUserScore();
            for (int i = 0; i < users.Length; i++)
            {
                _userRank.Add(users[i]);
            }

            _userRank.Sort((x, y) => y.Score.CompareTo(x.Score));

            return _userRank;
        }

        [AllowAnonymous]
        [HttpGet("allusers")]
        public ActionResult<List<User>> UsersInfo()
        {
            var userRanks = OrderByScore().ToArray();
            List<User> userList = new List<User>();

            for (int i = 0; i < userRanks.Length; i++)
            {
                userRanks[i].Rank = i + 1;
                _userService.UpdateRankPosition(userRanks[i].Id, userRanks[i]);
                _levelService.setUserLevel(userRanks[i]);
                userList.Add(userRanks[i]);
            }
            
            return _userService.Get();
        }

        [HttpGet]
        public IActionResult UserStats()
        {
            var headerId = Request.Headers["id"];

            var user = _userService.Get(headerId);

            if (user == null)
            {
                return BadRequest();
            }

            return Ok(new
            {
                Id = user.Id,
                Username = user.Username,
                Email = user.Email,
                Level = user.Level,
                Score = user.Score,
                Rank = user.Rank,
                DailyChallenge = user.dailyChallenges
            });
        }
    }
}