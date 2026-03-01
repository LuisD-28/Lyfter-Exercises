user_number = 0
addition = 0
number_counter = 1

user_number = int(input("Ingrese un numero: "))

while number_counter <= user_number:
    addition += number_counter
    number_counter += 1

print(f"La suma de los numeros desde 1 hasta {user_number} es: {addition}")