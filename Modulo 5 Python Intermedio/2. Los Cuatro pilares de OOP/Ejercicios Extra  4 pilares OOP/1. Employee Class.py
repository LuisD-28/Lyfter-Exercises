class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    
    def promote(self, percentage: float):
        if percentage < 0:
            raise ValueError("Promotion percentage cannot be negative.")

        increase = self.salary * (percentage / 100)
        self.salary += increase
        
        return self.salary
    

employee = Employee("Roberto Carlos", 5000)

print(employee.name)  # Output: Roberto Carlos
print(employee.salary)  # Output: 5000

employee.promote(10)
print(employee.salary)  # Output: 5500.0