namespace API.Models
{
    public class POCDatabaseSettings : IPOCDatabaseSettings
    {
        public string UserCollectionName { get; set; }

        public string ChallengeCollectionName {get; set; }

        public string ConnectionString { get; set; }

        public string DatabaseName { get; set; }
    }

    public interface IPOCDatabaseSettings
    {
        string UserCollectionName { get; set; }

        public string ChallengeCollectionName {get; set; }

        string ConnectionString { get; set; }

        string DatabaseName { get; set; }
    }
}