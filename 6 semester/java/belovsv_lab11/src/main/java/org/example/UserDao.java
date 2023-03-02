
package org.example;

/**
 * DAO-класс для работы с данными пользователей
 */
public interface UserDao {

    /**
     * Получение пользователя по имени
     *
     * @param name - имя для поиска
     * @return найденный пользователь
     */
    User getById(int id);

    /**
     * Создание нового пользователя
     *
     * @param user - данные пользователя
     */
    void create(User user);
    void drop(int id);
    void change(User user);
}