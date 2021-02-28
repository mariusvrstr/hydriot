using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Hydriot.Web.Data
{
    public class DbInitializer
    {
        public static void Initialize(ApplicationDbContext context)
        {
            context.Database.EnsureCreated();

            /* 
                // Look for any students.
                if (context.Nodes.Any())
                {
                    return;   // DB has been seeded
                }
            */

            // Addd seed data

            context.SaveChanges();
        }
    }
}
