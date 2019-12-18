using System;
using API.Models;
using System.Collections.Generic;

namespace API.Services
{
    public class RankService
    {
        private readonly UserService _userService;
        private List<User> _userRank;

        public RankService(UserService userService)
        {
            _userService = userService;
            _userRank = new List<User>();
        }

        public List<User> GetAllUserScore()
        {
            var users = _userService.Get().ToArray();

            for(int i = 0; i < users.Length; i++){
                _userRank.Add(users[i]);
            }

            _userRank.Sort((x, y) => y.Score.CompareTo(x.Score));

            return _userRank;
        }
    }
}