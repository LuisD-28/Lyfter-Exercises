def validate_numbers(func):
    def review(*args):
        for valor in args:
            if not isinstance(valor, (int, float)):
                return 'Error: todos los parametros deben ser numeros'
        return func(*args)
    return review



@validate_numbers
def add(a, b):
    return a + b


print(add(3, 4))
print(add(3, 'Hola'))