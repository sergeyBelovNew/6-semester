package org.example;

import org.example.menu.CarOperations;
import org.example.menu.Menu;
import org.example.menu.UserOperations;
import org.example.dao.CarDao;
import org.example.dao.UserDao;
import org.example.models.Car;
import org.example.models.User;

import java.util.Scanner;

public class Entry {

    private static final Scanner commandScanner = new Scanner(System.in);

    private static String command = "";

    public static void runTask12() {
        Scanner intScanner = new Scanner(System.in);
        System.out.println("Нажмите 1 если хотите работать с таблицей CARS, если хотите работать с USER, то 2."
                + "\nДля работы со связью - другую цифру");
        int choose = intScanner.nextInt();
        if (choose == 1) runCar();
        else runUser();
    }

    public static void runCar() {
        while (!command.equals("end")) {

            if (command.equals("1")) {
                CarOperations.createRaw();
            } else if (command.equals("2")) {
                CarOperations.getCar();
            } else if (command.equals("3")) {
                CarOperations.dropCar();
            } else if (command.equals("4")) {
                System.out.println("Введите id:");
                Scanner idScanner = new Scanner(System.in);
                int id = idScanner.nextInt();

                CarDao carDao = new CarDao();
                Car car = carDao.getById(id);
                CarOperations.change(car);
            } else if (command.equals("5")) {
                CarOperations.createTable();
            }
            Menu.printMenuCar();
            command = commandScanner.nextLine();
        }

    }

    private static void runUser() {
        while (!command.equals("end")) {

            if (command.equals("1")) {
                UserOperations.createRaw();
            } else if (command.equals("2")) {
                UserOperations.getUser();
            } else if (command.equals("3")) {
                UserOperations.dropUser();
            } else if (command.equals("4")) {
                System.out.println("Введите id:");
                Scanner idScanner = new Scanner(System.in);
                int id = idScanner.nextInt();

                UserDao userDao = new UserDao();
                User user = userDao.getById(id);
                UserOperations.change(user);
            } else if (command.equals("5")) {
                UserOperations.createTable();
            }
            Menu.printMenuUser();
            command = commandScanner.nextLine();
        }

    }

}


