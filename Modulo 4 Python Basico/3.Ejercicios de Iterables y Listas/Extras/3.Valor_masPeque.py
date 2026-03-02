userNumber_list = []
userNumber_count = 0

while userNumber_count < 6:
    userNumber_input = int(input(f"Ingrese el numero {userNumber_count + 1} de 6 : "))

    userNumber_list.append(userNumber_input)
    userNumber_count += 1

minNumber = userNumber_list[0]
for i in userNumber_list:
    if i < minNumber:
        minNumber = i

print("Los numeros ingresados son: ", userNumber_list)
print(f'El menor valor es: {minNumber}')