import csv

def open_csv_file(CVS_path):

    with open(CVS_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        headers = True
        for row in reader:
            if headers:
                headers = False
                continue
            print(f'Nombre: {row[0]}')
            print(f'Género: {row[1]}')
            print(f'Desarrollador: {row[2]}')
            print(f'Clasificación ESRB: {row[3]}')
            print('-----------------------')

        # with open(CVS_path, newline='', encoding='utf-8') as file:
        #     reader = csv.DictReader(file)
        #     for row in reader:
        #         for header, value in row.items():
        #             print(f'{header}: {value}')
        #         print('-----------------------')


def main():
    CVS_path = 'videojuegos.csv'
    print('-----------------------')
    open_csv_file(CVS_path)


if __name__ == "__main__":
    main()
