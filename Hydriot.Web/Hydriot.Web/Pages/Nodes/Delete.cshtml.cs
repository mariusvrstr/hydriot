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
    public class DeleteModel : PageModel
    {
        private readonly Hydriot.Web.Data.ApplicationDbContext _context;

        public DeleteModel(Hydriot.Web.Data.ApplicationDbContext context)
        {
            _context = context;
        }

        [BindProperty]
        public Node Node { get; set; }

        public async Task<IActionResult> OnGetAsync(Guid? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            Node = await _context.Nodes.FirstOrDefaultAsync(m => m.Id == id);

            if (Node == null)
            {
                return NotFound();
            }
            return Page();
        }

        public async Task<IActionResult> OnPostAsync(Guid? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var nodesRepo = new NodeRepository(_context);
            nodesRepo.Remove(id.Value);
            nodesRepo.Save();

            // TODO: Update repo to async

            return RedirectToPage("./Index");
        }
    }
}
