userNumber_list = []
user_number = 0
index = 0

while index < 10:
    user_number = int(input(f'Ingrese el numero {index+1}: '))
    userNumber_list.append(user_number)
    index += 1

print(f'Lista de numeros ingresados: {userNumber_list}')

for i, record in enumerate(userNumber_list):
    if record == max(userNumber_list):
        print(f'El numero mayor es: {record} y se encuentra en la posicion: {i+1}')
        moved_number = userNumber_list.pop(i)
        userNumber_list.insert(0, moved_number)
        print(f'Lista de numeros con el numero mayor al inicio: {userNumber_list}')