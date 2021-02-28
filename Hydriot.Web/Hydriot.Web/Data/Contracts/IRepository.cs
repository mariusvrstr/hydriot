using System;
using System.Collections.Generic;
namespace Hydriot.Web.Data.Contracts
{
    public interface IRepository<T>
           where T : IEntity
    {
        T GetById(Guid id);
        IList<T> FindAll();
        void Add(T entity);
        T Update(Guid id, T entity);
        void Remove(Guid id);
        void Save();
    }
}
