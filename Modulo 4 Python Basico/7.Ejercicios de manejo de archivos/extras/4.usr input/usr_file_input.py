def usr_file_input():
    while True:
        usr_input = input('Ingrese un texto: ')

        with open('testtext.txt', 'a', encoding='utf-8') as f:
            f.write(usr_input + '\n')

        with open('testtext.txt', encoding='utf-8') as f:
            content = f.read()
            print(content)

def main():
    usr_file_input()


if __name__ == "__main__":
    main()