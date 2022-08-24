def main():
    entrada = input("Ingrese los paises separados por comas: ")
    paises = entrada.split(",")
    paises = set(map(lambda x : x.strip(), paises)) // para remover espacios vacios ingresados por el usuario
    paises = sorted(paises)
    print(f'Los paises son {",".join(paises)}')

if __name__ == "__main__":
    main()