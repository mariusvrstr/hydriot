using System;
using System.Collections.Generic;

namespace Hydriot.Web.Models
{
    public class NodeData
    {
        public NodeData(Guid id, IEnumerable<SensorData> sensors)
        {
            Id = id;
            Sensors = sensors;
        }

        public Guid Id { get; set; }

        public IEnumerable<SensorData> Sensors { get; set; } = new List<SensorData>();


        public void UpdateSensorsData(IEnumerable<SensorData> latestData)
        {

        }

    }
}
