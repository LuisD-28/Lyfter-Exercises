userWords_List = []
four_letterList = []
userNumber_count = 0

while userNumber_count < 5:
    userWords_input = input(f"Ingrese la palabra {userNumber_count + 1} de 5 : ")

    userWords_List.append(userWords_input)
    userNumber_count += 1

print("Las palabras ingresadas son: ", userWords_List)

four_letters = [i for i in userWords_List if len(i) >= 4]
four_letterList.append(four_letters)


print(f'Las palabras con 4 letras o mas son: {four_letters}')