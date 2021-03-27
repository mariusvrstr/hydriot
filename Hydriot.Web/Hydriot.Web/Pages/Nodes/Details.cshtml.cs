using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;
using Hydriot.Web.Data.Repositories;

namespace Hydriot.Web.Pages.Nodes
{
    public class DetailsModel : PageModel
    {
        private readonly Hydriot.Web.Data.ApplicationDbContext _context;

        public DetailsModel(Hydriot.Web.Data.ApplicationDbContext context)
        {
            _context = context;
        }

        public Node Node { get; set; }

        public async Task<IActionResult> OnGetAsync(Guid? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var nodesRepo = new NodeRepository(_context);
            Node = nodesRepo.GetById(id.Value);

            if (Node == null)
            {
                return NotFound();
            }
            return Page();
        }
    }
}
