def mi_decorador(func):
    def wrapper(*args):
        print('Parametros: ', args)
        result = func(*args)
        print('Retorno: ', result)
        return result
    return wrapper

@mi_decorador
def multiply(a, b):
    return a * b

multiply(3, 5)




# def mi_decorador(func):
#     def orden():
#         print('Antes de ejecutar la funcion')
#         func()
#         print('Despues de ejecutar la funcion')
    
#     return orden


# @mi_decorador
# def saludar():
#     print('Hola Mundo')


# saludar()


