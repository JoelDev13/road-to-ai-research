import random

def main():
    numero_secreto = random.randint(1, 10)
    user = int(input("Ingrese un numero: "))

    while user != numero_secreto:
        print("El numero es diferente")
        user = int(input("Intente de nuevo: "))

    print(f"Adivinaste el número {numero_secreto}.")

if __name__ == "__main__":
    main()




if __name__ == "__main__":
    main()