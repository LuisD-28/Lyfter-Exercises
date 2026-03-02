def list_converter():
    while True:
        integer_list = []
        usr_num = 0
        while usr_num < 5:
            try:
                usr_input = input(f'Ingrese un numero ({usr_num + 1} de 5): ')
                
                
                usr_input_to_integer = int(usr_input)
                print(f'"{usr_input}" convertido a {usr_input_to_integer}')

                integer_list.append(usr_input_to_integer)
                usr_num += 1


            
            except ValueError:
                print(f"No se pudo convertir el valor '{usr_input}'")
        
        print(integer_list)
        break

        








def main():

    list_converter()


if __name__ == "__main__":
    main()