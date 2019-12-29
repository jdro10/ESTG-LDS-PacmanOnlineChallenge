using System;
using Xunit;
using System.Text;
using API.Controllers;
using API.Services;
using API.Models;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net;
using System.Collections.Generic;

namespace Tests
{
    public class UnitTest1
    {
        private static readonly HttpClient client = new HttpClient();

        [Fact]
        public void TestRouteAllUsers()
        {
            HttpWebRequest webRequest = (HttpWebRequest)WebRequest
                                           .Create("https://localhost:5001/api/user");
            HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();

            Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        }

        [Fact]
        public void TestRouteUsersRanks()
        {
            HttpWebRequest webRequest = (HttpWebRequest)WebRequest
                                           .Create("https://localhost:5001/api/ranks/allusers");
            HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();

            Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        }
    }
}
