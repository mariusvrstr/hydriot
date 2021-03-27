using Hydriot.Web.Authentication;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;
using Hydriot.Web.Data.Repositories;
using Hydriot.Web.Models;
using Hydriot.Web.Monitor;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Hydriot.Web.Controller
{
    [Route("api/[controller]")]
    [ApiController]
    public class NodeController : ControllerBase
    {

        private readonly NodeRepository _nodesRepo;

        public NodeController(ApplicationDbContext context)
        {
            _nodesRepo = new NodeRepository(context);
        }


        [HttpGet("{nodeId}")]
        [BasicAuthorization]
        public ActionResult<Node> GetNode(Guid nodeId)
        {
            var node = _nodesRepo.GetById(nodeId);

            if (node == null)
            {
                return NotFound();
            }

            return node;
        }

        [HttpGet("GetNodeSensorData/{nodeId}")]
        [BasicAuthorization]
        public ActionResult<NodeData> GetNodeSensorData(Guid nodeId)
        {
            var node = _nodesRepo.GetById(nodeId);

            if (node == null)
            {
                return NotFound();
            }

            var latestNodeData = NodeCache.Instance.GetLatestNodeSensorReadings(nodeId);

            return latestNodeData;
        }

        [HttpPost]
        [BasicAuthorization]
        public ActionResult<Guid> RegisterNewNode([FromBody] string name)
        {
            // Get the underlying account

            // Create a new node to the database for this account

            // Add to the in-memory cache

            // Return the ID

            throw new NotImplementedException();
        }



        [HttpPut("UpdateNodeSensors/{nodeId}")]
        [BasicAuthorization]
        public ActionResult<NodeData> UpdateNodeSensors(Guid nodeId, [FromBody] IEnumerable<SensorData> sensors)
        {
            var foundNode = _nodesRepo.GetById(nodeId);

            // TODO: Check that node is part of curren tuser account

            if (foundNode == null)
            {
                throw new InvalidProgramException($"Cannot update an node [{nodeId}] that does not yet exist. First register the node.");
            }

            var latestNodeData = new NodeData(nodeId, sensors);
            NodeCache.Instance.UpdateSensorReadings(latestNodeData);

            var mergedNodeData = NodeCache.Instance.GetLatestNodeSensorReadings(nodeId);

            return mergedNodeData;
        }
    }
}
