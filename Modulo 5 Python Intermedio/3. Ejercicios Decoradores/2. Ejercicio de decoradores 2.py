def validate_numbers(func):
    def review(*args):
        for valor in args:
            if not isinstance(valor, (int, float)):
                raise Exception('Error: todos los parametros deben ser numeros')
        return func(*args)
    return review



@validate_numbers
def add(a, b):
    return a + b

try:
    print(add(3, 4))
    print(add(3, 'Hola'))
except Exception as e:
    print(e)