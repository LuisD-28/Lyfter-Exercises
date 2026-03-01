numOne = 0
numtwo = 0
numthree = 0
thirty = 30


numOne = int(input("Ingrese el primer número: "))
numTwo = int(input("Ingrese el segundo número: "))
numThree = int(input("Ingrese el tercer número: "))

if numOne == thirty or numTwo == thirty or numThree == thirty:
    print("Correcto hay un numero 30")
elif numOne + numTwo + numThree == thirty:
    print("Correcto la suma de los numeros es 30")
else:    
    print("Incorrecto no hay un numero 30 ni la suma de los numeros es 30")