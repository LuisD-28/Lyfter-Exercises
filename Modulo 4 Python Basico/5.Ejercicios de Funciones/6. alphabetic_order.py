def alphabetic_order(alph_list):
    new_list = sorted(alph_list)
    print('String ordenada:')

    string = ""
    for i, list in enumerate(new_list):
        if i > 0:
            string += "-"
        string += list

    return string


def split_string(string):
    string_toList = string.split("-")
    print('Lista:')
    return string_toList

def main():
    string = 'python-variable-funcion-computadora-monitor'
    alph_list = split_string(string)
    print(alph_list)
    ordered_list = alphabetic_order(alph_list)
    print(ordered_list)


if __name__ == "__main__":
    main()
