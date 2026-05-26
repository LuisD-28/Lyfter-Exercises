-- SQLite

-- INSERT INTO products (code, name, price, entry_date, brand, stock_available, category_id)
-- VALUES
-- ('P006', 'Audífonos Bluetooth', 89.99, '2026-05-16', 'Sony', 40, 3),
-- ('P007', 'Barra de sonido', 149.99, '2026-05-17', 'Samsung', 12, 1),
-- ('P008', 'Escritorio de oficina', 249.99, '2026-05-18', 'Ikea', 7, 2),
-- ('P009', 'Lámpara LED', 29.99, '2026-05-19', 'Philips', 50, 2),
-- ('P010', 'Laptop ultrabook', 999.99, '2026-05-20', 'HP', 5, 1),
-- ('P011', 'Apple Magic Keyboard', 129.99, '2026-05-21', 'Apple', 15, 1);

-- Todos los productos 
SELECT * from products;

-- Productos con precio mayor a 50
SELECT * FROM products WHERE price > 50; -- le reduje el precio a 50 para mostrar más resultados

-- Productos que contienen "apple" en el nombre
SELECT * FROM products WHERE name LIKE '%apple%';

-- Top 5 productos más caros
SELECT * FROM products ORDER BY price DESC LIMIT 5;
