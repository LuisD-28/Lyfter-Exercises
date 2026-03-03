import json

def load_pokes():

    with open('D:\\lyfter\\Modulo 4 Python Basico\\9.Ejercicios con JSON\\extras\\pokemons.json', 'r', encoding='utf-8') as f:
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