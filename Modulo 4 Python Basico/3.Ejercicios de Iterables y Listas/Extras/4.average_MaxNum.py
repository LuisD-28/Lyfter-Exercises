userNumber_list = []
userNumber_count = 0

while userNumber_count < 6:
    userNumber_input = int(input(f"Ingrese el numero {userNumber_count + 1} de 6 : "))

    userNumber_list.append(userNumber_input)
    userNumber_count += 1

print("Los numeros ingresados son: ", userNumber_list)

average_lisNumber = sum(userNumber_list) / len(userNumber_list)
max_lisNumber = max(userNumber_list)
average_NewList = [i for i in userNumber_list if i > average_lisNumber]

print(f'El promedio de los numeros ingresados es: {average_lisNumber}')
print(f'El numero mayor de los ingresados es: {max_lisNumber}')
print(f'Lista con los numeros mayores al promedio: {average_NewList}')
