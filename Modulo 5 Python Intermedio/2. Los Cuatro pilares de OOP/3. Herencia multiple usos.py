#Extender clases sin modificar el código original
class vehicle:
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        print("engine started.")

class vehicle_light(vehicle):
    def turn_on_lights(self):
        print("lights turned on.")


auto = vehicle_light("Toyota")
auto.start_engine()
auto.turn_on_lights()

#Herencia múltiple con metodos del mismo nombre (uso de MRO)
#En python, la herencia múltiple se resuelve utilizando el método de resolución de orden (MRO). cuando varias clases tienen el mismo metodo, python sigue el orden de herencia para determinar cuál método ejecutar. el orden se determina por la secuencia en la que se definen las clases.

class A:
    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C(A, B):
    pass

c = C()
c.greet()  # Esto imprimirá "Hello from class A" debido al MRO
print(C.mro()) # Esto muestra el orden de resolución de métodos para la clase C