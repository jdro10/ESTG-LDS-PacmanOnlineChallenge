using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;

namespace API.Controllers
{
    [Route("api/ranks")]
    [ApiController]
    public class RankController : ControllerBase
    {
        private readonly RankService _rankService;
        private List<User> _userRank;
        private readonly UserService _userService;

        public RankController(RankService rankService, UserService userService)
        {
            _rankService = rankService;
            _userRank = new List<User>();
            _userService = userService;
        }

        private User[] OrderByScore(){

            var users = _rankService.GetAllUserScore(); 
            for(int i = 0; i < users.Length; i++){
                _userRank.Add(users[i]);
            }

            _userRank.Sort((x, y) => y.Score.CompareTo(x.Score));
            
            return users;
        
        }

        [AllowAnonymous]
        [HttpGet]
        public User[] GetUserRanks()
        {
            var userRanks = OrderByScore();

            for(int i = 0; i < userRanks.Length; i++)
            {
                userRanks[i].Rank = i+1;
                _userService.UpdateRankPosition(userRanks[i].Id, userRanks[i]);
            }

            return userRanks;
        }
    }
}