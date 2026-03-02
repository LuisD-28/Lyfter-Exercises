def file_management():
    txt_list = []
    txtfile = get_files(txt_list)

    with open('textfile2.txt', 'w', encoding='utf-8') as w:
        w.write(txtfile.replace('\n', ' '))

    with open('textfile2.txt', encoding='utf-8') as file:
        txtstring = file.read()
        print(txtstring)


def get_files(txt_string):
    path_first_file = 'textfile1.txt'
    with open(path_first_file, encoding='utf-8') as file:
        txt_string = file.read()

    print(f'{txt_string}')

    return txt_string










def main():
    file_management()


if __name__ == "__main__":
    main()