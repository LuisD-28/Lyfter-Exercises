import json
import os

def load_pokes():

    Base_dir = os.path.dirname(os.path.abspath(__file__))
    path_pokeJSON_file = os.path.join(Base_dir, 'pokemons.json')
    
    with open(path_pokeJSON_file, 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

        sum_by_type = {}
        count_by_type = {}

        for p in pokemons:
            level = p['level']
            for poke_type in p ['type']:
                sum_by_type[poke_type] = sum_by_type.get(poke_type, 0) + level
                count_by_type[poke_type] = count_by_type.get(poke_type, 0) + 1
        
        for poke_type in sum_by_type:
            average = sum_by_type[poke_type] / count_by_type[poke_type]

            print(f'Tipo: {poke_type} -> promedio de nivel: {average:.1f}')

def main():

    load_pokes()



if __name__ == "__main__":
    main()