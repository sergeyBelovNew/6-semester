package org.example;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner commandScanner = new Scanner(System.in);
        String command = "";

        while (!command.equals("end")) {

            if (command.equals("1")) {
                create();
            } else if (command.equals("2")) {
                getUser();
            } else if (command.equals("3")) {
                dropUser();
            } else if (command.equals("4")) {
                System.out.println("Введите id:");
                Scanner idScanner = new Scanner(System.in);
                int id = idScanner.nextInt();

                UserDao userDao = new UserDaoImpl();
                User user = userDao.getById(id);
                change(user);
            }

            printMenu();
            command = commandScanner.nextLine();
        }
    }

    private static void create() {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);
        User user = new User();

        System.out.println("Введите id:");
        user.setId(intScanner.nextInt());

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

        UserDao userDao = new UserDaoImpl();
        userDao.create(user);
        System.out.println("Пользователь добавлен");
    }

    private static void getUser() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        UserDao userDao = new UserDaoImpl();
        User user = userDao.getById(id);
        System.out.println("Найден пользователь: " + user);
    }

    private static void dropUser() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        UserDao userDao = new UserDaoImpl();
        userDao.drop(id);
        System.out.println("Удален пользователь: ");
    }

    private static void change(User user) {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);

        System.out.println("Введите id:");
        user.setId(intScanner.nextInt());

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

        UserDao userDao = new UserDaoImpl();
        userDao.create(user);
        System.out.println("Пользователь добавлен");
    }

    private static void printMenu() {
        System.out.println("Введите команду:");
        System.out.println("1) Добавить пользователя.");
        System.out.println("2) Получить пользователя.");
        System.out.println("3) Удалить пользователя.");
        System.out.println("4) Изменить пользователя.");
        System.out.println("end) Выход.");
    }
}