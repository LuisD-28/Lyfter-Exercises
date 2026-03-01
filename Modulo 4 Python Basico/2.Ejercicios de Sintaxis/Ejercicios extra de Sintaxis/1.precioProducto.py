product_price = 0
discount = 0
final_price = 0
discount_rate = 0


product_price = int(input("Ingrese el precio del producto: "))

if product_price < 100:
    discount = product_price * 0.02
    discount_rate = 2
else:
    discount = product_price * 0.1
    discount_rate = 10

final_price = product_price - discount

print(f"El descuento aplicado es: {discount_rate}%({discount}) y el precio final es: {final_price}")

