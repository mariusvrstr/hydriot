using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Hydriot.Web.Data;
using Hydriot.Web.Data.Entities;
using Hydriot.Web.Data.Repositories;

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

            var nodesRepo = new NodeRepository(_context);
            nodesRepo.Add(Node);

            //TODO: Add async save to repo
            //await _context.SaveChangesAsync();

            nodesRepo.Save();

            return RedirectToPage("./Index");
        }
    }
}
