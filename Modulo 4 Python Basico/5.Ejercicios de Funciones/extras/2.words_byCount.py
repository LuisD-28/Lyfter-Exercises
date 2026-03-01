def wordsby_Count():

    usr_wordList = get_usrwords()
    userCount_filter = int(input('Ingrese el numero de letras minimas en la palabra:'))

    filter = [w for w in usr_wordList if len(w) >= userCount_filter]
    print(filter)

    return True


def get_usrwords():
    user_wordList = []
    i = 0
    while i < 5:
        user_words = input(f'Ingrese una palabra ({i+1} de 5): ')
        user_wordList.append(user_words)
        i += 1

    return user_wordList


def main():
    wordsby_Count()


if __name__ == "__main__":
    main()