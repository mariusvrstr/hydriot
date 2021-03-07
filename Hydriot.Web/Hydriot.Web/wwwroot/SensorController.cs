using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Hydriot.Web.Models;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Hydriot.Web.wwwroot
{
    [Route("api/[controller]")]
    [ApiController]
    public class SensorController : ControllerBase
    {
        [HttpGet]
        public List<string> Get()
        {
            return new List<string> { "Hello", "World" };
        }
        
        /*

        // POST api/<SensorController>
        [HttpPost]
        [Route("UpdateSensorReading")]
        public void UpdateSensorReading([FromBody] SensorReadings value)
        {

        }

        */

    }
}
