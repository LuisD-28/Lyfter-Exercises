products = [
        {
            "name": "Monitor",
            "category": "Electrónica",
            "price": 200
        },    
        {
            "name": "Teclado",
            "category": "Electrónica",
            "price": 50
        },
        {   
            "name": "Silla",
            "category": "Muebles",
            "price": 120
        },
        {
            "name": "Mesa",
            "category": "Muebles",
            "price": 180
        },
        {
            "name": 
            "Mouse",
            "category": "Electrónica",
            "price": 25
        },
]

category_totaList= {}

for product in products:
    category = product["category"]
    price = product["price"]
    
    if category in category_totaList:
        category_totaList[category] += price
    else:
        category_totaList[category] = price

print(category_totaList)
