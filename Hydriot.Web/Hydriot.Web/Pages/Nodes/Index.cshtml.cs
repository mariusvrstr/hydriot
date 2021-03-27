using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;

namespace Hydriot.Web.Pages.Nodes
{
    public class IndexModel : PageModel
    {
        private readonly Hydriot.Web.Data.ApplicationDbContext _context;

        public IndexModel(Hydriot.Web.Data.ApplicationDbContext context)
        {
            _context = context;
        }

        public IList<Node> Node { get;set; }

        public async Task OnGetAsync()
        {
            Node = await _context.Nodes.ToListAsync();
        }
    }
}
