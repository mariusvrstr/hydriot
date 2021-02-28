using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Hydriot.Web.Data.Entities
{
    public class Node
    {
        public Guid Id { get; set; }

        public string DeviceName { get; set; }

        public string DeviceId { get; set; }

        public DateTime RegisteredDate { get; set; }

        public DateTime LastConnected { get; set; }

        public bool IsEnabled { get; set; }

        public bool IsDeleted { get; set; }

    }
}
