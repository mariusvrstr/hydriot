using Hydriot.Web.Data.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Hydriot.Web.Data.Repositories
{
    public class NodeRepository : RepositoryBase<Node>
    {
        public NodeRepository(ApplicationDbContext dataContext) : base(dataContext)
        {
        }
    }
}
