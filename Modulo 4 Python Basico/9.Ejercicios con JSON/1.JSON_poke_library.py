import json

def save_new_poke():
    with open('pokemons.json', 'r', encoding='utf-8') as f:
        pokemons = json.load(f)


    print('Ingrese la informacion del pokemon que deasea agregar a la libreria. \n')
    language = input('En que idioma ingresara el nombre del pokemon?: ')      
    name = input('Nombre: ')
    while True:
        try:
            level = int(input('Nivel: '))
            break
        except ValueError:
            print('Error: debes ingresar un numero entero')
            continue



    types = []
    print('Ingresa el tipo o tipos del Pokémon si es el caso (escribe "fin" para terminar): ')
    while True:
        type = input('Tipo: ').strip()
        if type.lower() == "fin":
            break
        if type:
            types.append(type)
            

    baseStats = getBase_stats()
        
    languagename = {
        language : name
    }

    newpoke = {
        "name": languagename,
        "level": level,
        "type": types,
        "base": baseStats
    }

    pokemons.append(newpoke)

    with open('pokemons.json', 'w', encoding='utf-8') as f:
        json.dump(pokemons, f, indent=4, ensure_ascii=False)
        print(f'\nPokemon: {name} agregado a la libreria con exito')
    



def getBase_stats():
        while True:
            print('\nIngrese los stats base del pokemon: ')
            try:
                hp = int(input('HP: '))
                attack = int(input('Attack: '))
                defense = int(input('Defense: '))
                sp_attack = int(input('Sp. Attack: '))
                sp_defense = int(input('Sp. Defense: '))
                speed = int(input('Speed: '))
            except ValueError:
                print(f'input invalido solo numeros enteros')
                continue
            baseStats = {
                "HP": hp, 
                "Attack": attack, 
                "Defense": defense, 
                "Sp. Attack": sp_attack, 
                "Sp. Defense": sp_defense, 
                "Speed": speed
            }
            return baseStats


def main():
    save_new_poke()
    while True:
        try:
            option = input('Desea agregar otro pokemon? escribe "si" o "no": ').strip().lower()
            if option not in ('s','n','si','no'):
                print('---------Opcion invalida---------')
                continue
            if option in ('s','si'):
                save_new_poke()
            else:
                print('Proceso terminado')
                break
        except ValueError as e:
            print(e)
            continue 


if __name__ == "__main__":
    main()