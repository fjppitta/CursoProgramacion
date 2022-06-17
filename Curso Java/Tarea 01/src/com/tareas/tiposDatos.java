package com.tareas;

/**
 * El siguiente programa corresponde a la primer tarea del curso de Java básico
 * consiste en imprimir todos los tipos de datos vistos durante la primer sessión.
 */

public class tiposDatos {

    public static void main(String[] args) {

        // Tipos de Datos
        // Numericos

        byte numeroByte=1;
        short numeroShort=345;
        int numeroInt=24;
        long numeroLong=16234;

        float numeroFloat = 2.3f;
        double numeroDouble=4.55d;

        System.out.println("Número byte: "+numeroByte);
        System.out.println("Número short: "+numeroShort);
        System.out.println("Número int: "+numeroInt);
        System.out.println("Número Long: "+numeroLong);

        System.out.println("Número Float: "+numeroFloat);
        System.out.println("Número Double: "+numeroDouble);

        // Texto

        char textoChar = 'c';
        String textoString = "Esto es una cadena";

        System.out.println("Texto Char: "+textoChar);
        System.out.println("Texto String: "+textoString);

        // Booleans

        boolean booleanoVerdadero=true;
        boolean booleanoFalso=false;

        System.out.println("Booleano Verdadero: "+booleanoVerdadero);
        System.out.println("Booleano Falso: "+booleanoFalso);



    }


}
