import csv

def open_csv(CVS_path, usr_input):
    with open(CVS_path, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file) 
        # print(reader.fieldnames)
        for row in reader:
            if row["Clasificación ESRB"] == usr_input:
                for header, value in row.items():
                    print(f'{header}: {value}')
                print('-----------------------')



def main():
    CVS_path = '..\\videojuegos.csv'
    usr_input = input('Ingrese la clasificacion ESRB que desea buscar: ')
    print('-----------------------')
    open_csv(CVS_path,usr_input)


if __name__ == "__main__":
    main()
