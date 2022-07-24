print("Ingrese su edad: ")
# La linea de abajo puede tener errores en tiempo de ejecucion
edad = int(input())

# Tambien se debe verificar edades no posibles
if(edad < 18):
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")