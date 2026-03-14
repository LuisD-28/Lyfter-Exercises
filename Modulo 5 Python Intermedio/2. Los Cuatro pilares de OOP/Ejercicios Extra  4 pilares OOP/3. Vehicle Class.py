class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return (f'Marca: {self._brand}, Año: {self._year}')
    

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        Vehicle.__init__(self, brand, year)
        self.doors = doors

    def get_info(self):
        base_info = Vehicle.get_info(self)
        i_str = (f'{base_info}, Puertas: {self.doors}')
        return i_str
    

class Motorcycle(Vehicle):
    def __init__(self, brand, year, moto_type):
        Vehicle.__init__(self, brand, year)
        self.motor_type = moto_type

    def get_info(self):
        base_info = Vehicle.get_info(self)
        i_str = (f'{base_info}, Tipo: {self.motor_type}')
        return i_str
    

Vehicle1 = Car('Toyota', 2020, 4)
vehicle2 = Motorcycle('Yamaha', 2022, 'Deportiva')

print(Vehicle1.get_info())
print(vehicle2.get_info())       