def get_usrNumbers(user_numberList):
    i = 0
    while i < 10:
        user_numbers = int(input(f'Ingrese el numero {i+1}: '))
        user_numberList.append(user_numbers)
        i += 1

    prime_list = []
    n = 0
    for n in user_numberList:
        if get_primenumbers(n):
            prime_list.append(n)
            
    print(f'Lista de numeros primos: {prime_list}')
    return user_numberList



def get_primenumbers(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True



def main():
    user_numberList = []
    get_usrNumbers(user_numberList)
    print(f'Lista de numeros Ingresados: {user_numberList}')



if __name__ == "__main__":
    main()

