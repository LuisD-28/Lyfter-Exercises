keys_toRemove = ['access_level', 'age']

employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for i in keys_toRemove:
    employee.pop(i)

print(employee)
