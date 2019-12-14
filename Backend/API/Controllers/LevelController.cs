using API.Models;
using Microsoft.AspNetCore.Mvc;

namespace API.Controllers
{
    public class LevelController : ControllerBase
    {
        public int setLevel(User user)
        {
            user.Level = 0;

            if(user.Score > 1000)
            {
                return 1;
            }

            return 0;
        }

    }
}