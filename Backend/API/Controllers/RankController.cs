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

        public RankController(RankService rankService)
        {
            _rankService = rankService;
        }

        [AllowAnonymous]

        [HttpGet]
        public ActionResult<List<User>> Get() =>
            _rankService.GetAllUserScore();

        [HttpGet("teste")]
        public ActionResult<List<User>> GetRank() =>
            _rankService.UserPosition();
        
    }
}