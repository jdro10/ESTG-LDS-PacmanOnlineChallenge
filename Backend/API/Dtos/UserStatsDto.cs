using API.Models;

namespace API.Dtos
{
    public class UserStatsDto
    {
        public string Id { get; set; }

        public string Username { get; set; }

        public string Email { get; set; }

        public int Level { get; set; }

        public int Score { get; set; }

        public int Rank { get; set; }

        public DailyChallenge[] dailyChallenges { get; set; }
    }
}