package org.example;

import javax.persistence.*;

@Entity
@Table(name = "TRAINS")
public class TrainEntity {

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTravelDate() {
        return travelDate;
    }

    public void setTravelDate(String travelDate) {
        this.travelDate = travelDate;
    }

    public int getСarNumber() {
        return сarNumber;
    }

    public void setСarNumber(int сarNumber) {
        this.сarNumber = сarNumber;
    }

    @Id
    @Column(name = "ID", nullable = false)
    private int id;

    @Column(name = "TRAVEL_DATA", nullable = false)
    private String travelDate;

    @Column(name = "CAR_DATA")
    private int сarNumber;
}