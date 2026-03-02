import json

def load_pokes():

    with open('pokemons.json', 'r', encoding='utf-8') as f:
        pokemons = json.load(f)

        sum_by_type = {}
        count_by_type = {}

        for p in pokemons:
            level = p['level']
            for type in p ['type']:
                sum_by_type[type] = sum_by_type.get(type, 0) + level
                count_by_type[type] = count_by_type.get(type, 0) + 1
        
        for type in sum_by_type:
            average = sum_by_type[type] / count_by_type[type]

            print(f'Tipo: {type} -> promedio de nivel: {average}')

def main():

    load_pokes()



if __name__ == "__main__":
    main()