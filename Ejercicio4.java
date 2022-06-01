public class Main {

    public static void main(String[] args) {

        // Primera parte IF
        System.out.println("Primera parte IF");
        var numeroIf = 0;
        if (numeroIf > 0) {
            System.out.println("El número es positivo");
        } else if (numeroIf < 0) {
            System.out.println("El número es negativo");
        } else {
            System.out.println("El número es cero");
        }

        // Segunda parte While
        System.out.println("\nSegunda parte While");
        var numeroWhile=1;
        while (numeroWhile<3){
            System.out.println(numeroWhile);
            numeroWhile=numeroWhile+1;
        }

        // Tercera parte Do-While
        System.out.println("\nTercera parte Do-While");
        numeroWhile=3;
        do {
            System.out.println(numeroWhile);
            numeroWhile=numeroWhile+1;
        }while (numeroWhile<3);

        // Cuarta parte For
        System.out.println("\nCuarta parte For");
        //var numeroFor;

        for (int numeroFor=0;numeroFor<=3;numeroFor++){
            System.out.println(numeroFor);
        }

        //Quinta parte Switch
        System.out.println("\nQuinta parte Switch");
        var estacion="primavera";

        switch (estacion){
            case "primavera":
                System.out.println("Es Primavera");
                break;
            case "verano":
                System.out.println("Es Verano");
                break;
            case "otoño":
                System.out.println("Es Otoño");
                break;
            case "invierno":
                System.out.println("Es Invierno");
                break;
            default:
                System.out.println(estacion);

        }

    }
}
