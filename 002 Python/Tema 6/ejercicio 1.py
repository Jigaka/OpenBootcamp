class Vehiculo:
    color = "blanco"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = "100"
    cilindrada = "1.5"

    def __str__(self):
        print("Instancia de coche")
        print("color =", self.color)
        print("ruedas = ", self.ruedas)
        print("puertas = ", self.puertas)
        print("velocidad =", self.velocidad)
        print("cilindrada =", end=" ")
        return self.cilindrada

coche = Coche()
print(coche)