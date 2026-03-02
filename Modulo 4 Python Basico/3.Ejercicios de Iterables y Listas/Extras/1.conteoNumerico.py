userNumber_list = []
userNumber_count = 0

while userNumber_count == 0:
    userNumber = int(input("Ingrese un numero (o 0 para terminar): "))
    if userNumber == 0:
        userNumber_count = 1
    else:
        userNumber_list.append(userNumber)

print("Los numeros ingresados son: ", userNumber_list)

userNumeber_choice = int(input("Ingrese el numero que desea buscar: "))
if userNumeber_choice in userNumber_list:
    print(f'El numero {userNumeber_choice} se encuentra en la lista y aparece {userNumber_list.count(userNumeber_choice)} veces.')
else:    
    print(f'El numero {userNumeber_choice} no se encuentra en la lista.')