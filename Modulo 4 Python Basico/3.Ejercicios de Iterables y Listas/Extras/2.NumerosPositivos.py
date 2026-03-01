userNumber_list = []
userNumber_count = 0
positive_number_count = True

while userNumber_count < 6:
    userNumber_input = int(input(f"Ingrese el numero {userNumber_count + 1} de 6 : "))
    if userNumber_input > 0:
        userNumber_list.append(userNumber_input)
        userNumber_count += 1

    else:
        if userNumber_input <= 0:

            userNumber_list.append(userNumber_input)
            userNumber_count += 1
            

            # print("Hay al menos un numero negativo o cero")

negative_number = [i for i in userNumber_list if i < 0]
zero_number = [i for i in userNumber_list if i == 0]    

if len(negative_number) > 0 or len(zero_number) > 0:
    print("Hay al menos un numero negativo o cero")
            

print("Los numeros ingresados son: ", userNumber_list)