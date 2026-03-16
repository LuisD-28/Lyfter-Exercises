def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        return func(*args)
    return wrapper


@repeat_twice
def greetings(name):
    print(f'Hello, {name}')



greetings('Pedro')