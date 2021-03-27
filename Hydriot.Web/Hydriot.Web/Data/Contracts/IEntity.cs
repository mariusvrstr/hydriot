using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Hydriot.Web.Data.Contracts
{
    public interface IEntity
    {
        Guid Id { get; set; }
    }
}
