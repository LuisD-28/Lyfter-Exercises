number_one = int(input('Ingrese el primer numero: '))
number_two = int(input('Ingrese el segundo numero: '))
number_three = int(input('Ingrese el tercer numero: '))

if number_one > number_two and number_one > number_three:
    print(f'El numero mayor es {number_one}')
elif number_two > number_one and number_two > number_three:
    print(f'El numero mayor es {number_two}')
elif number_three > number_one and number_three > number_two:
    print(f'El numero mayor es {number_three}')