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
        [HttpPost]
        public ActionResult<DailyChallenge> Create(DailyChallenge challenge)
        {
            _dailyChallengeService.Create(challenge);

            return Ok(new
            {
                DayOfWeek = challenge.DayOfWeek,
                Description = challenge.Description,
                Points = challenge.Points
            });       
        }

        [HttpGet]
        public ActionResult<List<DailyChallenge>> Get() =>
            _dailyChallengeService.Get();
    }
}