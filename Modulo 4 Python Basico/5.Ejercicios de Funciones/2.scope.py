global_variable = 'Hi?'


def second_function():
    print('Second function executed')
    global global_variable
    global_variable = global_variable + 'Aloh?'
    print (global_variable)
    
    


def main():
    print('First function executed')    
    second_function()

if __name__ == "__main__":
    main()