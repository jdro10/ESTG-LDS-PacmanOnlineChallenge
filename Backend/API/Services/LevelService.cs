using API.Models;
using System;

namespace API.Services
{
    public class LevelService
    {
        private int[] levelsArray;
        private readonly UserService _userService;

        public LevelService(UserService userService)
        {
            levelsArray = new int[100];
            levelsArray[0] = 1000;
            Levels();
            _userService = userService;
        }
        public void Levels()
        {
            for (int i = 1; i < levelsArray.Length; i++)
            {
                levelsArray[i] = levelsArray[i - 1] + 1000;
            }
        }

        public void setUserLevel(User user)
        {
            var userToUpdate = _userService.GetByName(user.Username);
            var userScore = userToUpdate.Score;
            int firstDigit = (int)(userScore.ToString()[0]) - 48;
            
            int i = 0;

            while(i != 99)
            {
                if(userScore < 1000)
                {
                    userToUpdate.Level = 0;
                    _userService.UpdateLevel(userToUpdate.Id, userToUpdate);
                    break;
                }
                if (levelsArray[i] <= userScore && levelsArray[i+1] > userScore)
                {
                    userToUpdate.Level = i+1;
                    _userService.UpdateLevel(userToUpdate.Id, userToUpdate);
                    break;
                }
                i++;
            }
        }
    }
}