User_number = 0
User_number_counter = 1

user_number = int(input("Ingrese un numero: "))

print(f"Tabla de multiplicar del numero {user_number}:")

while User_number_counter <= 12:
    result = user_number * User_number_counter
    print(f"{user_number} x {User_number_counter} = {result}")
    User_number_counter += 1
