using Hydriot.Web.Models;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;

namespace Hydriot.Web.Monitor
{
    /*
     * ======================================================================================================================
     * Warning: In scaled environments where application is not run in a single instance this will need to be moved to SQL
     * ======================================================================================================================
    */

    public class NodeCache
    {
        private static readonly object _lock = new object();

        private static NodeCache _instance;

        public static NodeCache Instance
        {
            get
            {
                if (_instance != null) return _instance;

                lock (_lock)
                    if (_instance == null)
                    {
                        var tempInstance = new NodeCache();
                        tempInstance.Initialize();
                        System.Threading.Thread.MemoryBarrier();
                        _instance = tempInstance;
                    }

                return _instance;
            }
        }

        public ConcurrentDictionary<Guid, NodeData> NodeList { get; set; }


        public void Initialize() 
        {
            NodeList = new ConcurrentDictionary<Guid, NodeData>();
        }

        public void UpdateSensorReadings(NodeData newData)
        {
            var missingSensors = new List<SensorData>();

            if (NodeCache.Instance.NodeList.TryGetValue(newData.Id, out NodeData cachedNode))
            {
                foreach (var sensor in newData.Sensors)
                {
                    var existingSensor = cachedNode.Sensors.Where(x => x.Name == sensor.Name && x.Type == sensor.Type).FirstOrDefault();

                    if (existingSensor == null)
                    {
                        missingSensors.Add(sensor);
                        continue;
                    }

                    existingSensor.StringValue = sensor.StringValue;
                    existingSensor.ReadTime = sensor.ReadTime;
                }

                if (missingSensors.Any())
                {
                    cachedNode.Sensors = cachedNode.Sensors.Concat(missingSensors);
                }
            }

            NodeList.AddOrUpdate(newData.Id, newData, (oldkey, oldvalue) => cachedNode);
        }

        public NodeData GetLatestNodeSensorReadings(Guid id)
        {
            return NodeList.GetValueOrDefault(id);
        }
    }
}
