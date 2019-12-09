using API.Models;
using MongoDB.Driver;
using System.Collections.Generic;
using System.Linq;

namespace API.Services
{
    public class UserService
    {
        private readonly IMongoCollection<User> _users;

        public UserService(IPOCDatabaseSettings settings)
        {
            var client = new MongoClient(settings.ConnectionString);
            var database = client.GetDatabase(settings.DatabaseName);

            _users = database.GetCollection<User>(settings.UserCollectionName);
        }

        public User Authenticate(string username, string password)
        {
            if(string.IsNullOrEmpty(username) || string.IsNullOrEmpty(password))
            {
                return null;
            }

            var user = GetByName(username);

            if(user == null)
            {
                return null;
            }

            if(password != user.Password)
            {
                return null;
            }

            return user;
        }

        public List<User> Get() => _users.Find(user => true).ToList();

        public User Get(string id) =>
            _users.Find<User>(user => user.Id == id).FirstOrDefault();

        public User GetByName(string username) =>
            _users.Find<User>(user => user.Username == username).FirstOrDefault();

        public User GetByEmail(string email) =>
            _users.Find<User>(user => user.Email == email).FirstOrDefault();

        public User Create(User user)
        {
            _users.InsertOne(user);
            return user;
        }

        public void Update(string id, User userIn) =>
            _users.ReplaceOne(user => user.Id == id, userIn);

        public void Remove(User userIn) =>
            _users.DeleteOne(user => user.Id == userIn.Id);

        public void Remove(string id) =>
            _users.DeleteOne(user => user.Id == id);
    }
}