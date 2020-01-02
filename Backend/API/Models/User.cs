using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace API.Models
{
    public class User
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("Username")]
        public string Username { get; set; }

        public string Email { get; set; }

        public string Password { get; set; }

        public byte[] PasswordHash { get; set; }

        public byte[] PasswordSalt { get; set; }

        public int Level { get; set; }

        public int Score { get; set; }

        public int Rank { get; set; }

        public string[] todayDoneChallenge { get; set; }

        public DailyChallenge[] dailyChallenges { get; set; }
    }
}