def add_values():
    usr_float_ist = []
    usr_count_input = 0
    while usr_count_input < 5:
        try:
            usr_value_input = input(f'Ingrese un numero ({usr_count_input + 1} de 5): ')

            usr_input_float = float(usr_value_input)
            print(f'{usr_input_float} sumado correctamente')

            usr_float_ist.append(usr_input_float)
            usr_count_input += 1


        except ValueError:
            print(f"Elemento invalido: '{usr_value_input}'")
        
    print(f'Total de la suma {sum(usr_float_ist)}')    









def main():
    add_values()

if __name__ == "__main__":
    main()