
using System;

namespace Hydriot.Web.Models
{
    public class SensorData
    {
        public string Name { get; set; }

        public BaseType Type { get; set; }

        public string StringValue { get; set; }

        public DateTime ReadTime { get; set; }
    }
}
