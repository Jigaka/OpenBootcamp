print("Ingrese el numero inicial: ")
numeroInicial = int(input())

print("Ingrese el numero final: ")
numeroFinal = int(input())

# TODO: verificar que numeroFinal sea mayor a numeroInicial

numerosImpares = []
for i in range(numeroInicial, numeroFinal):
    if(i % 2 == 1):
        numerosImpares.append(i)

print(numerosImpares)