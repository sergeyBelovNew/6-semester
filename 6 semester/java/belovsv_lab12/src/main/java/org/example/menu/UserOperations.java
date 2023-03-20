package org.example.menu;

import org.example.dao.UserDao;
import org.example.models.User;

import java.util.Scanner;

public class UserOperations {

    public static void createTable() {
        UserDao userDao = new UserDao();
        userDao.createTableUser();
    }

    public static void createRaw() {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);
        User user = new User();

        System.out.println("Введите id:");
        user.setIdUser(intScanner.nextInt());

        System.out.println("Введите имя:");
        user.setNameEmployer(strScanner.nextLine());

        System.out.println("Введите фамилию:");
        user.setSurname(strScanner.nextLine());

        System.out.println("Введите отчество:");
        user.setSecondName(strScanner.nextLine());

        System.out.println("Введите должность:");
        user.setPositionEmployer(strScanner.nextLine());

        System.out.println("Введите департамент:");
        user.setDepartment(strScanner.nextLine());

        System.out.println("Введите зарплату:");
        user.setSalary(intScanner.nextInt());

        UserDao userDao = new UserDao();
        userDao.createRaw(user);
        System.out.println("Пользователь добавлен");
    }

    public static void getUser() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        UserDao userDao = new UserDao();
        User user = userDao.getById(id);
        System.out.println("Найден пользователь: " + user);
    }

    public static void dropUser() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        UserDao userDao = new UserDao();
        userDao.drop(id);
        System.out.println("Удален пользователь: ");
    }

    public static void change(User user) {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);

        System.out.println("Введите id:");
        user.setIdUser(intScanner.nextInt());

        System.out.println("Введите имя:");
        user.setNameEmployer(strScanner.nextLine());

        System.out.println("Введите фамилию:");
        user.setSurname(strScanner.nextLine());

        System.out.println("Введите отчество:");
        user.setSecondName(strScanner.nextLine());

        System.out.println("Введите должность:");
        user.setPositionEmployer(strScanner.nextLine());

        System.out.println("Введите департамент:");
        user.setDepartment(strScanner.nextLine());

        System.out.println("Введите зарплату:");
        user.setSalary(intScanner.nextInt());

        UserDao userDao = new UserDao();
        userDao.createRaw(user);
        System.out.println("Пользователь добавлен");
    }
}
