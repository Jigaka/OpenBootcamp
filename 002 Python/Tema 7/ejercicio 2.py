from time import localtime

def main():
    horaActual = localtime().tm_hour
    minutoActual = localtime().tm_min
    if horaActual >= 19:
        print("Ya es hora de ir a casa")
    else: 
        if horaActual == 18:
            print("Faltan {} minutos para salir del trabajo".format(60 - minutoActual))
        else:
            print("Faltan {} horas y {} minutos para salir del trabajo".format(18 - horaActual, 60 - minutoActual))

if __name__ == "__main__":
    main()