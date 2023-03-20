package org.example;
import org.hibernate.HibernateException;

import javax.persistence.EntityManager;

public class TrainDao {
    public void createRaw(TrainEntity train) {
        try {
            EntityManager entityManager = DbConnection.getEntityManager();
            entityManager.getTransaction().begin();
            entityManager.persist(train);

            entityManager.getTransaction().commit();
        } catch (HibernateException ex) {
            throw new HibernateException(ex);
        }
    }

    public TrainEntity getTrain(int id) {
        EntityManager entityManager = DbConnection.getEntityManager();
        return entityManager.find(TrainEntity.class, id);
    }
}