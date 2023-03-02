package org.example;

public class User {

    private int id;

    private String nameEmployer;

    private String surname;

    private String secondName;

    private String positionEmployer;

    private String department;

    private int salary;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNameEmployer() {
        return nameEmployer;
    }

    public void setNameEmployer(String nameEmployer) {
        this.nameEmployer = nameEmployer;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public String getSecondName() {
        return secondName;
    }

    public void setSecondName(String secondName) {
        this.secondName = secondName;
    }

    public String getPositionEmployer() {
        return positionEmployer;
    }

    public void setPositionEmployer(String positionEmployer) {
        this.positionEmployer = positionEmployer;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name_employer='" + nameEmployer + '\'' +
                ", surname='" + surname + '\'' +
                ", secondName='" + secondName + '\'' +
                ", positionEmployer='" + positionEmployer + '\'' +
                ", department='" + department + '\'' +
                ", salary=" + salary +
                '}';
    }

}