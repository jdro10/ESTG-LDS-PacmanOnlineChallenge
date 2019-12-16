using API.Models;
using MongoDB.Driver;
using System.Collections.Generic;
using System.Linq;

namespace API.Services
{
    public class DailyChallengeService
    {
        private readonly IMongoCollection<DailyChallenge> _challenges;

        public DailyChallengeService(IPOCDatabaseSettings settings)
        {
            var client = new MongoClient(settings.ConnectionString);
            var database = client.GetDatabase(settings.DatabaseName);

            _challenges = database.GetCollection<DailyChallenge>(settings.ChallengeCollectionName);
        }

        public DailyChallenge Create(DailyChallenge challenge)
        {
            _challenges.InsertOne(challenge);
            
            return challenge;
        }

        public List<DailyChallenge> Get() => _challenges.Find(challenge => true).ToList();

        public DailyChallenge[] GetByDay(string day) {
            var challengesArray = _challenges.Find<DailyChallenge>(challenge => challenge.DayOfWeek == day).ToList().ToArray();

            return challengesArray;
        }
    }
}