import json

def load_poke_list():

    with open('pokemons.json', 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

        for p in pokemons:
            level = p.get('level')
            types = ', '.join(p.get('type'))
            stats = p.get('base')

            for language, name in p.get('name').items():
                print("---------- Pokémon ----------")
                print(f'Idioma: {language}')
                print(f'Nombre: {name}')
                print(f'Nivel: {level}')
                print(f'Tipo(s): {types}')
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