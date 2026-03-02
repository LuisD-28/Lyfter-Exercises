import json

def getpoke_by_type(usr_tipe_input):
    coincidence = False

    usr_tipe_input = usr_tipe_input.lower()

    with open('pokemons.json', 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

    for p in pokemons:
        types = p.get('type')
        alltypes = [t.lower() for t in types]

        if usr_tipe_input in alltypes:
            coincidence = True

    if coincidence == True:
        load_pokemon(usr_tipe_input)
    else:
        print(f'No se ecnontro ningun pokémon del tipo: {usr_tipe_input}')


def load_pokemon(usr_tipe_input):
    with open('pokemons.json', 'r', encoding='utf-8') as f:
        pokemons = json.load(f)
    
    print(f'Los pokemons que existen del tipo "{usr_tipe_input}" son: ')

    for p in pokemons:
        types = p.get('type')
        alltypes = [t.lower() for t in types]

        if usr_tipe_input in alltypes:
            for name in p.get('name').values():
                print(name)



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
        usr_tipe_input = input('Ingrese el tipo de pokemon desea buscar: ')
        getpoke_by_type(usr_tipe_input)
    
        if not new_search():
            print('Busqueda finalizada')
            break


if __name__ == "__main__":
    main()