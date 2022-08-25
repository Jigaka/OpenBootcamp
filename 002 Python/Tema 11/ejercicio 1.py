import sqlite3


def crearTabla():
    conn = sqlite3.connect("colegio.db")
    cursor = conn.cursor()

    queryCrearTabla = f'CREATE TABLE IF NOT EXISTS alumnos(id, nombre, apellido)'
    cursor.execute(queryCrearTabla)

    conn.commit()
    cursor.close()
    conn.close()

def rellenarTabla():
    conn = sqlite3.connect("colegio.db")
    cursor = conn.cursor()

    dataQueryInsertarAlumnos = [
        (1, "Jose", "Garcete"),
        (1, "Carlos", "Acosta"),
        (1, "Tobias", "Melgarejo"),
        (1, "Juan", "Perez"),
        (1, "Marciano", "Venus"),
        (1, "Jose", "Jolo"),
        (1, "Gago", "Gego"),
        (1, "Gulio", "Fenero")
    ]
    
    cursor.executemany("INSERT INTO alumnos VALUES(?,?,?)", dataQueryInsertarAlumnos)

    conn.commit()
    cursor.close()
    conn.close()

def obtenerDatos(nombre):
    conn = sqlite3.connect("colegio.db")
    cursor = conn.cursor()

    res = cursor.execute(f"SELECT * FROM alumnos WHERE nombre='{nombre}'")
    alumno = res.fetchone()

    cursor.close()
    conn.close()

    return alumno

def main():
    crearTabla()
    rellenarTabla()
    alumno = obtenerDatos("Jose")
    if alumno == None:
        print("No hay alumno con ese nombre")
    else:
        print(alumno)

if __name__ == "__main__":
    main()