class mathOps:

    def add(self, a, b):
        return a + b
    
    def average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    
    def divide(self, number1, number2):
        if number2 == 0:
            raise ValueError('You cannot divide by zero')
        elif not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
            raise TypeError('Both arguments must be numbers')
        return number1 / number2
    
