class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    

while True:
    try:
        height = float(input("Enter the height: "))
        width = float(input("Enter the width: "))
        R = Rectangle(width, height)
        print(f"Area: {R.get_area()}")
        print(f"Perimeter: {R.get_perimeter()}")
        break
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
