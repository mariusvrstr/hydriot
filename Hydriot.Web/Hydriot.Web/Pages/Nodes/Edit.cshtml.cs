using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;

namespace Hydriot.Web.Pages.Nodes
{
    public class EditModel : PageModel
    {
        private readonly Hydriot.Web.Data.ApplicationDbContext _context;

        public EditModel(Hydriot.Web.Data.ApplicationDbContext context)
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

        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see https://aka.ms/RazorPagesCRUD.
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.Attach(Node).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!NodeExists(Node.Id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return RedirectToPage("./Index");
        }

        private bool NodeExists(Guid id)
        {
            return _context.Nodes.Any(e => e.Id == id);
        }
    }
}
