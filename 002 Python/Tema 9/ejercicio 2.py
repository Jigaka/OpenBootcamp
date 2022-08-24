import sys
from functools import reduce

def main():
    if(len(sys.argv) != 2):
        print("El programa solo acepta un parametro: una lista")
        return
    
    
    lista = filter( lambda item: item.isdigit() , list(sys.argv[1]))
    lista = map(lambda item: int(item), lista)

    lista = filter(lambda item: item % 2 == 1, lista)
    print(f'La suma de los elementos impares es: {reduce(lambda acc, item: acc + item ,lista)}')

if __name__ == "__main__":
    main()