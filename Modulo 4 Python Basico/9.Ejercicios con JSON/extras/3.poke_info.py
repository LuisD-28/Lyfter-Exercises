import json
import os

def load_poke_list():
    
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    path_pokeJSON_file = os.path.join(Base_dir, 'pokemons.json')

    #por alguna extraña razon, al usar la ruta raiz no me funciona, por lo que tuve que usar la ruta completa
    with open(path_pokeJSON_file, 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

        for p in pokemons:
            stats = p.get('base')

            for name in p.get('name').values():
                print("---------- Pokémon ----------")
                print(f'Nombre: {name}')
                print(f'Stats:')
                print(f'  HP: {stats.get('HP')}')
                print(f'  Attack: {stats.get('Attack')}')
                print(f'  Defense: {stats.get('Defense')}')
                print(f'  Sp. Attack: {stats.get('Sp. Attack')}')
                print(f'  Sp. Defense: {stats.get('Sp. Defense')}')
                print(f'  Speed: {stats.get('Speed')}')


def main():
    load_poke_list()



if __name__ == "__main__":
    main() 