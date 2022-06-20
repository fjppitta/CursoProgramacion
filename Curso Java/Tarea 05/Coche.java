package com.tareas;

public class Coche {

    String modelo;
    String marca;
    String color;
    int puertas;

    public Coche() {
    }

    public Coche(String modelo, String marca, String color, int puertas) {
        this.modelo = modelo;
        this.marca = marca;
        this.color = color;
        this.puertas = puertas;
    }

    @Override
    public String toString() {
        return "Coche --> " +
                "Modelo='" + modelo + '\'' +
                ", Marca='" + marca + '\'' +
                ", Color='" + color + '\'' +
                ", Puertas=" + puertas +
                '.';
    }
}
