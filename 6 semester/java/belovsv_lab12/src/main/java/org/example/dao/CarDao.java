package org.example.dao;

import org.example.models.Car;
import org.example.utils.DbConnector;

import java.sql.*;


public class CarDao {

    private static final String CREATE_NEW_CARS_TABLE = "CREATE TABLE CARS (\n" +
            "ID INT NOT NULL,\n" +
            "COST INT NOT NULL,\n" +
            "MODEL VARCHAR,\n" +
            "COLOR VARCHAR,\n" +
            "PRIMARY KEY (ID),\n" +
            "UNIQUE (COST)\n" +
            ");";

    private static final String GET_BY_ID_QUERY = "SELECT * FROM CARS WHERE ID = ?;";
    private static final String INSERT_USER_QUERY = "INSERT INTO CARS(ID, COST, MODEL, COLOR) VALUES(?,?,?,?);";

    public void createTable() {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement preparedStatement = connection.prepareStatement(CREATE_NEW_CARS_TABLE);
            preparedStatement.execute();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }


    public Car getById(int id) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement selectStatement = connection.prepareStatement(GET_BY_ID_QUERY);
            selectStatement.setInt(1, id);
            ResultSet result = selectStatement.executeQuery();
            Car car = new Car();
            while (result.next()) {
                car.setId(result.getInt("id"));
                car.setCost(result.getInt("cost"));
                car.setModel(result.getString("model"));
                car.setColor(result.getString("color"));
            }
            return car;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public void createRaw(Car car) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement insertStatement = connection.prepareStatement(INSERT_USER_QUERY);
            insertStatement.setInt(1, car.getId());
            insertStatement.setInt(2, car.getCost());
            insertStatement.setString(3, car.getModel());
            insertStatement.setString(4, car.getColor());
            insertStatement.execute();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public void dropRaw(int id) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement dropStatement = connection.prepareStatement(GET_BY_ID_QUERY, ResultSet.TYPE_SCROLL_SENSITIVE,
                    ResultSet.CONCUR_UPDATABLE);
            dropStatement.setInt(1, id);
            ResultSet result = dropStatement.executeQuery();
            result.next();
            result.deleteRow();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public void change(Car car) {
        try (Connection connection = DbConnector.getConnection()) {
            PreparedStatement changeStatement = connection.prepareStatement(INSERT_USER_QUERY);
            changeStatement.setInt(1, car.getId());
            changeStatement.setInt(2, car.getCost());
            changeStatement.setString(3, car.getModel());
            changeStatement.setString(4, car.getColor());
            changeStatement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}

