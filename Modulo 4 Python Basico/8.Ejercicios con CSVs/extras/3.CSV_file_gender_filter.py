import csv

def open_csv(CVS_path):
    count = {}
    with open(CVS_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            gender = row.get('Género')
            if gender:
                count[gender] = count.get(gender, 0) + 1

    for gender, item in sorted(count.items()):
        print(f'{gender}: {item}')


def main():
    CVS_path = 'videojuegos.csv'
    print('Géneros encontrados: ')
    print('---------------------')
    open_csv(CVS_path)


if __name__ == "__main__":
    main()
