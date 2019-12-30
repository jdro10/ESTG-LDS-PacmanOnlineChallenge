using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;
using API.Dtos;

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

        private List<UserStatsDto> OrderByScore2(UserStatsDto[] usdto)
        {
            var users = usdto;

            for (int i = 0; i < users.Length; i++)
            {
                _userStatsDto.Add(users[i]);
            }

            _userStatsDto.Sort((x, y) => y.Score.CompareTo(x.Score));

            return _userStatsDto;
        }

        private void updateUserRanks()
        {
            var userRanks = OrderByScore().ToArray();

            for (int i = 0; i < userRanks.Length; i++)
            {
                userRanks[i].Rank = i + 1;
                _userService.UpdateRankPosition(userRanks[i].Id, userRanks[i]);
            }
        }

        [AllowAnonymous]
        [HttpGet("topten")]
        public ActionResult<UserStatsDto[]> UsersInfo()
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

            var userRanks2 = _userService.Get().ToArray();

            UserStatsDto[] userRanksDto = new UserStatsDto[userRanks2.Length];

            for (int i = 0; i < userRanks2.Length; i++)
            {
                userRanksDto[i] = new UserStatsDto();
                userRanksDto[i].Id = userRanks2[i].Id;
                userRanksDto[i].Username = userRanks2[i].Username;
                userRanksDto[i].Email = userRanks2[i].Email;
                userRanksDto[i].Level = userRanks2[i].Level;
                userRanksDto[i].Score = userRanks2[i].Score;
                userRanksDto[i].Rank = userRanks2[i].Rank;
                userRanksDto[i].dailyChallenges = userRanks2[i].dailyChallenges;
            }

            var listArray = this.OrderByScore2(userRanksDto).ToArray();

            UserStatsDto[] usdto = new UserStatsDto[10];

            for (int i = 0; i < listArray.Length; i++)
            {
                usdto[i] = listArray[i];
                if (i == 9)
                {
                    break;
                }
            }

            return usdto;
        }

        [AllowAnonymous]
        [HttpGet]
        public IActionResult UserStats()
        {
            this.updateUserRanks();

            var headerId = Request.Headers["id"];

            var user = _userService.Get(headerId);

            _levelService.setUserLevel(user);

            var user2 = _userService.Get(user.Id);

            if (user2 == null)
            {
                return BadRequest();
            }

            return Ok(new
            {
                Id = user2.Id,
                Username = user2.Username,
                Email = user2.Email,
                Level = user2.Level,
                Score = user2.Score,
                Rank = user2.Rank,
                DailyChallenge = user2.dailyChallenges
            });
        }
    }
}