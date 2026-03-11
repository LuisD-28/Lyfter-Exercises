class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def show_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return
        
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        return total
    
inventory = Inventory()

inventory.add_product(Product("Mouse", 50, 5))
inventory.add_product(Product("Teclado", 100, 3))
inventory.add_product(Product("Monitor", 300, 2))
inventory.add_product(Product("Impresora", 150, 4))
inventory.add_product(Product("Laptop", 1000, 1))
inventory.add_product(Product("Tablet", 200, 6))

print("Inventory:")
inventory.show_inventory()
print(f"\nTotal Inventory Value: {inventory.total_value()}")