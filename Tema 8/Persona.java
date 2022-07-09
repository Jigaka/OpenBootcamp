public class Persona {
    private String edad;
    private String nombre;
    private String telefono;

    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public static void main(String[] args) {
        Persona juan = new Persona();
        Persona jose = new Persona();
        Persona victor = new Persona();

        juan.setNombre("Juan");
        juan.setEdad("18");
        juan.setTelefono("0123456789");

        jose.setNombre("Jose");
        jose.setEdad("19");
        jose.setTelefono("0123456789");

        victor.setNombre("Victor");
        victor.setEdad("19");
        victor.setTelefono("0123456789");

        System.out.printf("Mi nombre es %s, tengo %s años y mi telefono es %s\n", juan.getNombre(), juan.getEdad(),
                juan.getTelefono());
        System.out.printf("Mi nombre es %s, tengo %s años y mi telefono es %s\n", jose.getNombre(), jose.getEdad(),
                jose.getTelefono());
        System.out.printf("Mi nombre es %s, tengo %s años y mi telefono es %s\n", victor.getNombre(), victor.getEdad(),
                victor.getTelefono());

    }
}
