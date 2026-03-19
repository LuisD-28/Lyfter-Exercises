from datetime import datetime

def validate_numbers(func):
    def wrapper(*args):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError('All parameters must be numeric')
        return func(*args)
    return wrapper
    

def log_call(func):
    def wrapper(*args):
        now = datetime.now()
        print(f'func: {func.__name__} - args: {args} - {now}')

        result = func(*args)

        print(f'Return: {result}')
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(a, b): 
    return a * b


multiply(8, 90)