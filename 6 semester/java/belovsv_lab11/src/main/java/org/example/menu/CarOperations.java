package org.example.menu;

import org.example.dao.CarDao;
import org.example.models.Car;

import java.util.Scanner;

public class CarOperations {

    public static void create() {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);
        Car car = new Car();

        System.out.println("Введите id:");
        car.setId(intScanner.nextInt());

        System.out.println("Введите модель:");
        car.setModel(strScanner.nextLine());

        System.out.println("Введите цвет:");
        car.setColor(strScanner.nextLine());

        CarDao carDao = new CarDao();
        carDao.create(car);
        System.out.println("Машина добавлена");
    }

    public static void getCar() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        CarDao carDao = new CarDao();
        Car car = carDao.getById(id);
        System.out.println("Найдена машина: " + car);
    }

    public static void dropCar() {

        System.out.println("Введите id:");
        Scanner idScanner = new Scanner(System.in);
        int id = idScanner.nextInt();

        CarDao carDao = new CarDao();
        carDao.drop(id);
        System.out.println("Удалена машина: ");
    }

    public static void change(Car car) {
        Scanner intScanner = new Scanner(System.in);
        Scanner strScanner = new Scanner(System.in);

        System.out.println("Введите id:");
        car.setId(intScanner.nextInt());

        System.out.println("Введите модель:");
        car.setModel(strScanner.nextLine());

        System.out.println("Введите цвет:");
        car.setColor(strScanner.nextLine());

        CarDao carDao = new CarDao();
        carDao.create(car);
        System.out.println("Машина измменина");
    }
}
