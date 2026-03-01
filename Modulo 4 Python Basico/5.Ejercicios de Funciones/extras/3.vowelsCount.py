def vowels_count():
    get_usrword = input('Ingrese una palabra o frase: ')

    vowels = sum(1 for w in get_usrword.lower() if w in 'aeiou')

    print(f'El numero de vocales en el texto ingresado es: {vowels}')


    return True

def main():
    vowels_count()


if __name__ == "__main__":
    main()