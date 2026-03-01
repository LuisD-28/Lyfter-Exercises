def second_function(local_variable):
    print('Second function executed')
    print(local_variable)

def third_function(number_list):
    print('Third function executed')
    print(number_list)


def main():
    print('First function executed')
    local_variable = 'This is a local variable'
    number_list = [1,9,23,38,54,76,102,135,180,200]
    second_function(local_variable)
    third_function(number_list)

if __name__ == "__main__":
    main()