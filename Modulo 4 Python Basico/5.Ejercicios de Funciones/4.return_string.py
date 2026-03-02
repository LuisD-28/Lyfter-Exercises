def ordered_string(my_string):
    print('string original:', my_string)
    inverted_string = my_string[::-1] 

    return inverted_string

def main():
    my_string = 'sever la atircse euf esarf atse'
    string = ordered_string(my_string)
    
    print(string)


if __name__ == "__main__":
    main()