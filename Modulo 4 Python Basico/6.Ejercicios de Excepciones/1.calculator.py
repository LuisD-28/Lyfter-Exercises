def Calculator():
    actual_result = None
    while True:
        print('---------Calculadora----------')
        print('1) Sumar')
        print('2) Restar')
        print('3) Multiplicar')
        print('4) Dividir')
        print('5) Borrar Resultado')

        option = input('Elige la operacion que deseas realizar: ')

        if option not in ('1','2','3','4','5'):
            print('Opcion Invalida')
            input("Enter para continuar...") 
            continue
        if option == '5':
            actual_result = None 
            print("Número actual borrado.") 
            input("Enter para continuar...") 
            continue

        try:
            if actual_result != None:
                a = actual_result
                print (f'Numero actual: {a}')
                b = float(input('Segundo numero: '))
            else:
                a = float(input('Primer numero: '))
                b = float(input('Segundo numero: '))
        except ValueError:
            print('Input invalido, solo numeros.')
            continue

        if option == '1':
            result = add(a,b)
        elif option == '2':
            result = subtract(a,b)
        elif option == '3':
            result = multiply(a,b)
        elif option == '4':
            result = divide(a,b)
        # elif option == '5':

        actual_result = result

        print(f'Resultado: {result}')
        input("Enter para continuar...") 
        continue

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        a / b
    except:
        print('Error: No puedes dividir entre cero')
        return 0
    return a / b


def main():
    Calculator()


if __name__ == "__main__":
    main()