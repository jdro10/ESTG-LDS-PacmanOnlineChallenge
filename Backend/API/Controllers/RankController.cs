using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using API.Dtos;
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
        private List<UserStatsDto> _userStatsDto;
        private readonly UserService _userService;
        private readonly LevelService _levelService;

        public RankController(RankService rankService, UserService userService, LevelService levelService)
        {
            _rankService = rankService;
            _userRank = new List<User>();
            _userStatsDto = new List<UserStatsDto>();
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

        private ActionResult<List<UserStatsDto>> OrderByScore2(UserStatsDto[] usdto)
        {
            var users = usdto;

            for (int i = 0; i < users.Length; i++)
            {
                _userStatsDto.Add(users[i]);
            }

            _userStatsDto.Sort((x, y) => y.Score.CompareTo(x.Score));

            return _userStatsDto;
        }

        [AllowAnonymous]
        [HttpGet("allusers")]
        public ActionResult<List<UserStatsDto>> UsersInfo()
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
            
            var userRanks2 =  _userService.Get().ToArray();

            UserStatsDto[] userRanksDto = new UserStatsDto[userRanks2.Length];

            for(int i = 0; i < userRanks2.Length; i++)
            {
                userRanksDto[i] = new UserStatsDto();
                userRanksDto[i].Id = userRanks2[i].Id;
                userRanksDto[i].Username =userRanks2[i].Username;
                userRanksDto[i].Email = userRanks2[i].Email;
                userRanksDto[i].Level = userRanks2[i].Level;
                userRanksDto[i].Score = userRanks2[i].Score;
                userRanksDto[i].Rank = userRanks2[i].Rank;
                userRanksDto[i].dailyChallenges = userRanks2[i].dailyChallenges;
            }

            var listToReturn = this.OrderByScore2(userRanksDto);

            return listToReturn;
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