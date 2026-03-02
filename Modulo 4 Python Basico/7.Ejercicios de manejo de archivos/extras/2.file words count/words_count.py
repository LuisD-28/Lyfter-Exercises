def get_files():

    with open('textfile.txt', encoding='utf-8') as file:
        txtcontent = file.read()
        words = txtcontent.split()
        
    
    print(f'Este archivo contiene "{len(words)}" palabras')





def main():
    get_files()


if __name__ == "__main__":
    main()