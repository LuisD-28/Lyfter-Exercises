def get_usrInfo():
    while True:
        try:
            usrName = input('Ingrese su nombre: ')
            if usrName.isdigit():
                raise ValueError('El nombre no puede ser un numero.')
            
            usrAge = input('Ingrese su edad: ')
            if not usrAge.isdigit():
                raise ValueError('Numero no valido.')

            
            print(f'Hola {usrName}, su edad es {usrAge}')

            break

        except ValueError as e:
            print(e)





def main():
    get_usrInfo()


if __name__ == "__main__":
    main()