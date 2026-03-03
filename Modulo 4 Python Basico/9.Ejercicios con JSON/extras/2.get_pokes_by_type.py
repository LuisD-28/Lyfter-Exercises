import json
import os

def getpoke_by_type(usr_type_input):
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    path_pokeJSON_file = os.path.join(Base_dir, 'pokemons.json')

    poke_list = []

    usr_type_input = usr_type_input.lower()

    with open(path_pokeJSON_file, 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

    for p in pokemons:
        types = p.get('type')
        alltypes = [t.lower() for t in types]

        if usr_type_input in alltypes:
            for name in p.get('name').values():
                lvl = p.get('level')
                poke_list.append(f'{name} (Level: {lvl})')



#################################################################################################
    if poke_list:
        print(f'Los pokemons que existen del tipo "{usr_type_input}" son: ')
        for poke in poke_list:
            print(poke)
    else:
        print(f'No se encontraron pokemons del tipo "{usr_type_input}"')




def new_search():
    while True:
        try:
            option = input('Desea realizar otra busqueda? escribe "si" o "no": ').strip().lower()
            if option not in ('s','n','si','no'):
                print('---------Opcion invalida---------')
                continue
            if option in ('s','si'):
                return True
            elif option in ('n','no'):
                return False
        except ValueError as e:
            print(e)
            continue



def main():
    while True:
        usr_type_input = input('Ingrese el tipo de pokemon desea buscar: ')
        getpoke_by_type(usr_type_input)
    
        if not new_search():
            print('Busqueda finalizada')
            break


if __name__ == "__main__":
    main()