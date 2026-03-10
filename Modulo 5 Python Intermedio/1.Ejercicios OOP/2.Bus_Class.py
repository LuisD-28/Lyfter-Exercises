class Person:
	def __init__(self, name):
		self.name = name
		self.age = 0

# person_1 = Person("John")
# print(person_1.age)
# print(person_1.name)



class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        
    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} has boarded the bus.')
        else:
            print('the bus is full, cannot add more passengers.')
    def descend_passenger(self, person):
        if person in self.passengers:
            self.passengers.pop(0)
            print(f'{person.name} has left the bus.')

            

bus = Bus(2)
person_1 = Person("John")
person_2 = Person("Raul")
person_3 = Person("Roberto")

bus.add_passenger(person_1)
bus.add_passenger(person_2)
bus.add_passenger(person_3)

bus.descend_passenger(person_1)
bus.descend_passenger(person_2)
bus.descend_passenger(person_3)