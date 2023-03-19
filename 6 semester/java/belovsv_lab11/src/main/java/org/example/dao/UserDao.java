
package org.example.dao;

import org.example.models.User;

/**
 * DAO-класс для работы с данными пользователей
 */
public interface UserDao {

    User getById(int id);

    void create(User user);
    void drop(int id);
    void change(User user);
}