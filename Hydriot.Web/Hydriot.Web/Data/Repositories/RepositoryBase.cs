using Hydriot.Web.Data.Contracts;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore.ChangeTracking;

namespace Hydriot.Web.Data.Repositories
{
    public abstract class RepositoryBase<T> : IRepository<T>
        where T : class, IEntity
    {
        private DbContext Context { get; set; }
        private DbSet<T> _table { get; set; }

        protected RepositoryBase(DbContext dataContext)
        {
            this.Context = dataContext;
            _table = Context.Set<T>();
        }

        public T GetById(Guid id)
        {
            return _table.Find(id);
        }

        public IList<T> FindAll()
        {
            return _table.ToList();
        }

        public void Add(T entity)
        {
            if (entity.Id == Guid.Empty)
            {
                entity.Id = Guid.NewGuid();
            }

            _table.Add(entity);
        }

        public T Update(Guid id, T entity)
        {
            if (id != entity.Id)
            {
                throw new Exception($"Invalid update request. The ID [{id}] is different from the object provided");
            }

            _table.Attach(entity);
            Context.Entry(entity).State = EntityState.Modified;

            return entity;
        }

        public void Remove(Guid id)
        {
            var existing = _table.Single(a => a.Id == id);

            if (existing == null)
            {
                throw new DataMisalignedException($"Entity [{typeof(T)}] with ID [{id}]");
            }

            _table.Remove(existing);
        }

        public void Save()
        {
            Context.SaveChanges();
        }
    }
}
