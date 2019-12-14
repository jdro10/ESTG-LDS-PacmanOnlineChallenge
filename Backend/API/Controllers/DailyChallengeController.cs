using API.Models;
using API.Services;
using API.Helpers;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.Extensions.Options;
using Microsoft.AspNetCore.Authorization;

namespace API.Controllers
{
    [Route("api/challenge")]
    [ApiController]
    public class DailyChallengeController : ControllerBase
    {
        private readonly DailyChallengeService _dailyChallengeService;
        private readonly AppSettings _appSettings;

        public DailyChallengeController(DailyChallengeService dailyChallengeService, IOptions<AppSettings> appSettings)
        {
            _dailyChallengeService = dailyChallengeService;
            _appSettings = appSettings.Value;
        }

        [AllowAnonymous]
        [HttpPost]
        public ActionResult<DailyChallenge> Create(DailyChallenge challenge)
        {
            _dailyChallengeService.Create(challenge);

            return CreatedAtRoute("GetChallenges", new { id = challenge.Id.ToString() }, challenge);            
        }

        [HttpGet]
        public ActionResult<List<DailyChallenge>> Get() =>
            _dailyChallengeService.Get();
    }
}