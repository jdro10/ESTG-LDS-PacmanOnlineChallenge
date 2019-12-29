using System;
using Xunit;
using API.Controllers;
using API.Services;
using API.Models;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net;

namespace Tests
{
    public class UnitTest1
    {

        [Fact]
        public void Test1()
        {
            HttpWebRequest webRequest = (HttpWebRequest)WebRequest
                                           .Create("https://localhost:5001/api/ranks/allusers");
            HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();

            Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        }
    }
}
