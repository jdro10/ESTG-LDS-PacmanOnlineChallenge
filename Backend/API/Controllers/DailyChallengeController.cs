using API.Models;
using API.Services;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Authorization;

namespace API.Controllers
{
    [Route("api/challenge")]
    [ApiController]
    public class DailyChallengeController : ControllerBase
    {
        private readonly DailyChallengeService _dailyChallengeService;

        public DailyChallengeController(DailyChallengeService dailyChallengeService)
        {
            _dailyChallengeService = dailyChallengeService;
        }

        [AllowAnonymous]
        [HttpGet("create")]
        public ActionResult<DailyChallenge> Create()
        {
            DailyChallenge[] dc1 = new DailyChallenge[7];
            DailyChallenge[] dc2 = new DailyChallenge[7];
            DailyChallenge[] dc3 = new DailyChallenge[7];

            for (int i = 0; i < 7; i++)
            {
                dc1[i] = new DailyChallenge();
                dc2[i] = new DailyChallenge();
                dc3[i] = new DailyChallenge();
                
                dc1[i].DayOfWeek = i.ToString();
                dc2[i].DayOfWeek = i.ToString();
                dc3[i].DayOfWeek = i.ToString();

                dc1[i].Description = "Play 1 game";
                dc1[i].Points = 500;

                dc2[i].Description = "Score 1000 points in a game";
                dc2[i].Points = 750;

                dc3[i].Description = "Win a multiplayer game";
                dc3[i].Points = 1000;
            }

            for (int i = 0; i < 7; i++)
            {
                _dailyChallengeService.Create(dc1[i]);
                _dailyChallengeService.Create(dc2[i]);
                _dailyChallengeService.Create(dc3[i]);
            }

            return Ok(new
            {
                result = "desafios criados"
            });
        }

        [HttpGet]
        public ActionResult<List<DailyChallenge>> Get() =>
            _dailyChallengeService.Get();
    }
}