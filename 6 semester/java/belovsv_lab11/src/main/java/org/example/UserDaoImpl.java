package org.example;

import javax.xml.transform.Result;
import java.sql.*;

public class UserDaoImpl implements UserDao {

    private static final String GET_BY_ID_QUERY = "SELECT * FROM USERDATA U WHERE U.ID = ?;";
    private static final String INSERT_USER_QUERY = "INSERT INTO USERDATA(ID, NAME_EMPLOYER, SURNAME," +
            " SECOND_NAME, POSITION_EMPLOYER , DEPARTMENT, SALARY) VALUES(?,?,?,?,?,?,?);";

    @Override
    public User getById(int id) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement selectStatement = connection.prepareStatement(GET_BY_ID_QUERY);
            selectStatement.setInt(1, id);
            ResultSet result = selectStatement.executeQuery();
            result.next();

            User user = new User();
            user.setId(result.getInt("id"));
            user.setNameEmployer(result.getString("name"));
            user.setSurname(result.getString("surname"));
            user.setSecondName(result.getString("secondName"));
            user.setPositionEmployer(result.getString("position"));
            user.setDepartment(result.getString("department"));
            user.setSalary(result.getInt("salary"));
            return user;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void create(User user) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement insertStatement = connection.prepareStatement(INSERT_USER_QUERY);
            insertStatement.setInt(1, user.getId());
            insertStatement.setString(2, user.getNameEmployer());
            insertStatement.setString(3, user.getSurname());
            insertStatement.setString(4, user.getSecondName());
            insertStatement.setString(5, user.getPositionEmployer());
            insertStatement.setString(6, user.getDepartment());
            insertStatement.setInt(7, user.getSalary());
            insertStatement.execute();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void drop(int id) {
        //need repair
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement dropStatement = connection.prepareStatement(GET_BY_ID_QUERY);
            dropStatement.setInt(1, id);
            ResultSet result = dropStatement.executeQuery();
            result.next();
            result.deleteRow();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void change(User user) {
        //need repair
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement changeStatement = connection.prepareStatement(INSERT_USER_QUERY);
            changeStatement.setInt(1, user.getId());
            changeStatement.setString(2, user.getNameEmployer());
            changeStatement.setString(3, user.getSurname());
            changeStatement.setString(4, user.getSecondName());
            changeStatement.setString(5, user.getPositionEmployer());
            changeStatement.setString(6, user.getDepartment());
            changeStatement.setInt(7, user.getSalary());
            changeStatement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}