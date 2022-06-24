public class Coche {
    private int numeroDePuertas = 0;

    public void aumentarPuertas() {
        numeroDePuertas++;
    }

    public static void main(String[] args) {
        Coche coche = new Coche();
        coche.aumentarPuertas();
        System.out.println(coche.numeroDePuertas);
    }
}
