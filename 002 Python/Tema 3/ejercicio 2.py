print("Ingrese su peso en kilogramos:")
peso = input()

print("Ingrese su estatura en metros")
estatura = input()

peso = float(peso)
estatura = float(estatura)

masaCorporal = peso / (estatura**2)
masaCorporal = round(masaCorporal, 2)
print("Tu índice de masa corporal es ", masaCorporal)