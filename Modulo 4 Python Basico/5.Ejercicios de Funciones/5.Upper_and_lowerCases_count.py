def upper_and_lower_cases_count(string):
    upper_count = 0 
    lower_count = 0
    
    for s in string:
        if s.isupper():
            upper_count += 1
        elif s.islower():
            lower_count += 1
            
    return upper_count, lower_count


def main():
    string = 'El Año Nuevo Lunar es el comienzo de un año cuyos meses son ciclos lunares'
    upper_count, lower_count = upper_and_lower_cases_count(string)
    print(f'There is {upper_count} upper cases and {lower_count} lower cases')


if __name__ == "__main__":
    main()