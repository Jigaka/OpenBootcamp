public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.edad = 21;
        cliente.nombre = "Jose";
        cliente.telefono = "145487954";
        cliente.credito = 1234567;

        Trabajador trabajador = new Trabajador();
        trabajador.edad = 22;
        trabajador.nombre = "Carlos";
        trabajador.telefono = "25456848";
        trabajador.salario = 456789;

        System.out.printf("Mi nombre es %s, tengo %d anhos, mi telefono es %s, tengo credito %s y soy de %s\n",
                cliente.nombre, cliente.edad, cliente.telefono, cliente.credito, Cliente.class);

        System.out.printf("Mi nombre es %s, tengo %d anhos, mi telefono es %s, mi salario %s y soy de %s\n",
                trabajador.nombre, trabajador.edad, trabajador.telefono, trabajador.salario, Trabajador.class);
    }
}
