import pickle

class Vehiculo:
    marca = ""
    cilindrada = ""

    def __init__(self, marca, cilindrada):
        self.marca = marca
        self.cilindrada = cilindrada

    def __str__(self):
        return f'Soy la clase vehiculo de marca {self.marca} con {self.cilindrada} de cilindrada'

def main():
    f = open("archivo.bin", "wb")
    v = Vehiculo("Toyota","2.0")
    pickle.dump(v, f)
    f.close()

    f = open("archivo.bin", "rb")
    v2 = pickle.load(f)
    f.close()

    print(v2)


if __name__ == "__main__":
    main()