my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
evenNum_list = []

print(f'lista de numeros: {my_list}')

for evenNum in my_list:
    if evenNum % 2 == 0:
        evenNum_list.append(evenNum)
        

print(f'lista de numeros pares: {evenNum_list}')