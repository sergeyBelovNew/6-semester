package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int choose = 0;
        System.out.println("Выберите сделать запись в бд(1), или получить запись (2), завершить работу программы 3");
        choose = intScanner.nextInt();
        while (choose != 3) {
            if (choose == 1) {
                createRaw();
            }
            else {
                System.out.println("Введите  id");
                getRaw(strScanner.nextInt());
            }
            System.out.println("Выберите сделать запись в бд(1), или получить запись (2), завершить работу программы 3");
            choose = strScanner.nextInt();
        }
    }

    public static void createRaw() {
        TrainEntity train = new TrainEntity();
        System.out.println("Введите id");
        train.setId(intScanner.nextInt());
        System.out.println("Введите дату поездки");
        train.setTravelDate(strScanner.nextLine());
        System.out.println("Введите номер машины");
        train.setСarNumber(intScanner.nextInt());
        TrainDao trainDao = new TrainDao();
        trainDao.createRaw(train);
    }

    public static void getRaw(int id) {
        TrainDao trainDao = new TrainDao();;
        System.out.println(trainDao.getTrain(id));
    }

    private static final Scanner intScanner = new Scanner(System.in);

    private static final Scanner strScanner = new Scanner(System.in);
}