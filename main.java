// package com.company;

public class Main {

    public static void main (String [] args){
        int resultado;
        int a=2;
        int b=3;
        int c=4;
        Coche miCoche = new Coche();

        // Primera parte
        resultado=sumadetres(a,b,c);
        System.out.println(resultado);

        // Segunda Parte
        miCoche.PonerPuerta();
        System.out.println(miCoche.puertas);

    }

    public static int sumadetres (int a, int b, int c){

        return a+b+c;
    }
}

class Coche{
    public int puertas=0;
    public void PonerPuerta(){
        this.puertas++;
    }
}
