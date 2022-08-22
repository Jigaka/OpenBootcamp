class Alumno():
    nombre = ""
    nota = 0

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = nota


alumno = Alumno()
alumno.setNombre("jose")
alumno.setNota(5)

print("Nombre del alumno:", alumno.nombre)
print("Nota:", alumno.nota)
print("Aprobado") if alumno.nota >= 2 else print("Reprobado")