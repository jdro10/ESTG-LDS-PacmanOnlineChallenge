using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace UsersAPI.Models
{
    public class User
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id {get; set;}

        [BsonElement("UserEmail")]
        public string UserEmail{get; set;}
        public string Password{get; set;}
    }
}