import random

number = int(input("Ingrese un numero del 1 al 10: "))
secret_number = random.randint(1, 10)


while number != secret_number:
    if number > 10:
        number = int(input("Numero invalido. Por favor ingrese un numero del 1 al 10: "))
    elif number != secret_number:
        print("Intenta de nuevo")
        number = int(input("Ingrese un numero del 1 al 10: "))

print("Felicidades Has adivinado el numero secreto")            
print(f'El numero secreto es {secret_number}')









