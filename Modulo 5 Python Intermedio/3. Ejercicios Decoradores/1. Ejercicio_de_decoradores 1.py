def mi_decorador(func):
    def orden():
        print('Antes de ejecutar la funcion')
        func()
        print('Despues de ejecutar la funcion')
    
    return orden


@mi_decorador
def saludar():
    print('Hola Mundo')


saludar()


