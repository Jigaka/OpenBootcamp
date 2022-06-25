public class Tema4 {

    public static void main(String[] args) {
        condicionales();
        cicloWhile();
        cicloDoWhile();
        cicloFor();
        controlSwitch();
    }

    private static void condicionales() {
        System.out.println("Apartado condicionales");
        System.out.println("----------------------------");
        int numeroif = 10;
        String valorNumero = null;
        if (numeroif < 0) {
            valorNumero = "negativo";
        } else if (numeroif > 0) {
            valorNumero = "positivo";
        } else {
            valorNumero = "0";
        }

        System.out.println("El valor es: " + valorNumero);
        System.out.println();
    }

    private static void cicloWhile() {
        System.out.println("Apartado while");
        System.out.println("----------------------------");
        int numeroWhile = 0;
        while (numeroWhile < 3) {
            System.out.println(numeroWhile);
            numeroWhile++;
        }
        System.out.println();
    }

    private static void cicloDoWhile() {
        System.out.println("Apartado do while");
        System.out.println("----------------------------");
        int numeroDoWhile = 0;
        do {
            System.out.println(numeroDoWhile);
            numeroDoWhile++;
        } while (numeroDoWhile < 1);
        System.out.println();
    }

    private static void cicloFor() {
        System.out.println("For");
        System.out.println("----------------------------");
        for (int numeroFor = 0; numeroFor < 3; numeroFor++) {
            System.out.println(numeroFor);
        }
        System.out.println();
    }

    private static void controlSwitch() {
        System.out.println("Apartado switch");
        System.out.println("----------------------------");
        String estacion = "diciembre";
        String msg = null;
        switch (estacion) {
            case "verano":
                msg = "Se está en la estacion de verano";
                break;
            case "otoño":
                msg = "Se está en la estacion de otoño";
                break;
            case "invierno":
                msg = "Se está en la estacion de invierno";
                break;
            case "primavera":
                msg = "Se está en la estacion de primavera";
                break;
            default:
                msg = "El valor de la variable no es una estacion";
                break;
        }
        System.out.println(msg);
        System.out.println();
    }
}
