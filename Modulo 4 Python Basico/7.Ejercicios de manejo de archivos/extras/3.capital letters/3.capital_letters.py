def file_func():

    with open('firstfile.txt', encoding='utf-8') as file1:
        content = file1.read().upper()

    with open('secondfile.txt', 'w', encoding='utf-8') as file2:
        file2.write(content)    
        
        print(content)
    









def main():
    file_func()

if __name__ == "__main__":
    main()