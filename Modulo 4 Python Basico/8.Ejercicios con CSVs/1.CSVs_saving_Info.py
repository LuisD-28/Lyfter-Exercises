import csv

def read_csv_file():
    vgame_inf_headers = ('Nombre',
                    'Género',
                    'Desarrollador',
                    'Clasificación ESRB',
    )
    try:
        with open('videojuegos.csv', 'r', encoding='utf-8') as file:
            exists = True
    except FileNotFoundError:
        exists = False

    with open('videojuegos.csv', 'a', newline='', encoding='utf-8') as file:
        if not exists:
            writer = csv.DictWriter(file, vgame_inf_headers)
            writer.writeheader()



def usr_input_save():

    print('Ingresa la informacion de los videojuegos que deseas almacenar \n')
    name = input('Nombre: ')
    gender = input('Género: ')
    Developer = input('Desarollador: ')
    classification = input('Clasificación ESRB: ')


    with open('videojuegos.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, gender, Developer, classification])
    print('Informacion guardada. \n')


def videogame_info():
        usr_input_save()
        while True:
            try:
                option = input('Deseas agregar otro juego? escribe "si" o "no": ').strip().lower()
                if option not in ('s','n','si','no'):
                    print('---------Opcion invalida---------')
                    continue
                if option in ('s','si'):
                    usr_input_save()
                else:
                    break
            except ValueError as e:
                print(e)
                continue
                




def main():
    read_csv_file()
    videogame_info()
    print('Proceso terminado')


if __name__ == "__main__":
    main()
























# import csv

# def read_csv_file():
#     vgame_inf_headers = ('Nombre',
#                         'Género',
#                         'Desarrollador',
#                         'Clasificación ESRB',
#     )

#     with open('videojuegos.csv', mode='w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, vgame_inf_headers)
#         writer.writeheader()



# def usr_input_save(name,gender,Developer,classification):
#     with open('videojuegos.csv', mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow([name, gender, Developer, classification])



# def videogame_info():
#         while True:
        
#             print('Ingresa la informacion de los videojuegos que deseas almacenar \n')
#             name = input('Nombre: ')
#             gender = input('Género: ')
#             Developer = input('Desarollador: ')
#             classification = input('Clasificación ESRB: ')
        
#             usr_input_save(name,gender,Developer,classification)
#             print('Informacion guardada. \n')
#             try:
#                 option = input('Deseas agregar otro juego? escribe "si" o "no": ').strip().lower()
#                 if option not in ('s','n','si','no'):
#                     print('Opcion invalida')
#                     option
#             except ValueError as e:
#                 print(e)
#                 continue
                




# def main():
#     read_csv_file()
#     videogame_info()
#     print('Proceso terminado')


# if __name__ == "__main__":
#     main()
