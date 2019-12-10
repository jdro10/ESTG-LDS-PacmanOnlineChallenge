using API.Models;
using API.Services;
using API.Helpers;
using API.Dtos;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.Extensions.Options;
using Microsoft.AspNetCore.Authorization;
using System.Text;
using System;
using Microsoft.IdentityModel.Tokens;
using System.Security.Claims;
using System.Security.Cryptography;


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

            return CreatedAtRoute("GetUser", new { id = challenge.Id.ToString() }, challenge);            
        }

        [HttpGet]
        public ActionResult<List<DailyChallenge>> Get() =>
            _dailyChallengeService.Get();
    }
}