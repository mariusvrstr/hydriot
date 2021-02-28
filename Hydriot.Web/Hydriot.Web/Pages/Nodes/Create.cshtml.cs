using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;

namespace Hydriot.Web.Pages.Nodes
{
    public class CreateModel : PageModel
    {
        private readonly Hydriot.Web.Data.ApplicationDbContext _context;

        public CreateModel(Hydriot.Web.Data.ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult OnGet()
        {
            return Page();
        }

        [BindProperty]
        public Node Node { get; set; }

        // To protect from overposting attacks, see https://aka.ms/RazorPagesCRUD
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.Nodes.Add(Node);
            await _context.SaveChangesAsync();

            return RedirectToPage("./Index");
        }
    }
}
