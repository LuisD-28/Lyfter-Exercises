INSERT INTO ejercicios_transacciones.Users (full_name, email)
VALUES ('Luis Tester', 'luis@test.com');

INSERT INTO ejercicios_transacciones.Products (name, price, stock)
VALUES 
('Laptop', 1200, 10),
('Mouse', 25, 50);


UPDATE ejercicios_transacciones.Products
SET stock = 5
WHERE product_id = 1;


SELECT * FROM ejercicios_transacciones.Products;
SELECT * FROM ejercicios_transacciones.Bills;
SELECT * FROM ejercicios_transacciones.BillProducts;