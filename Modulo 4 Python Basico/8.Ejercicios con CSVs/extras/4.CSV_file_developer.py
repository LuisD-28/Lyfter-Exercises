import csv

def open_csv(CVS_path):
    count = {}
    with open(CVS_path, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dev = row.get('Desarrollador')
            if dev:
                if dev not in count:
                    count[dev] = []

                count[dev].append(row)
    # for usr_input, games in count.items():
    #     print(f'{usr_input}: {games}')
    

    while True:
        usr_input = input('\n Ingrese el nombre de la desarolladora de videojuegos que desea buscar: ')
        games = count.get(usr_input)
        if games != None:
            print(f"\nVideojuegos desarrollados por {usr_input}:")
            print('---------------------------------------------')
            for game in games:
                name = game.get('Nombre')
                gender = game.get('Género')
                clasification = game.get('Clasificación ESRB')
                print(f' - {name} (Clasificación: {clasification}, Género: {gender})')
        else:
            print(f'No se encontraron resultados para: "{usr_input}"')
            continue




def main():
    CVS_path = 'videojuegos.csv'

    open_csv(CVS_path)


if __name__ == "__main__":
    main()
