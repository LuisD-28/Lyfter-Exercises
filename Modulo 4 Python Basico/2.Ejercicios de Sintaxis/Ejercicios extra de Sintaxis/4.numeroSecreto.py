import random

random_number = random.randint(1, 10)

user_number = int(input("Ingrese un numero entre 1 y 10: "))

while user_number != random_number:
    if user_number > 10:
        user_number = int(input("numero invalido. Por favor ingrese un numero del 1 al 10: "))
    else:
        print("Intenta de nuevo")
        user_number = int(input("Ingrese un numero entre 1 y 10: "))

print(f"¡Felicidades! Has adivinado el número secreto {random_number}.")
