def character_count():
    user_str = getUser_text()
    getusrCharacter_count(user_str)

    return True


def getUser_text():
    user_str = input('Ingrese una frase o texto: ')
    print(user_str)
    
    return user_str


def getusrCharacter_count(user_str):
    user_character = input('Ingrese el caracter que desea buscar: ')
    character = user_str.count(user_character)
    print(f'el character: {user_character} se a encontrado: {character} veces en el texto ingresado ')

    return True


def main():
    character_count()


if __name__ == "__main__":
    main()
