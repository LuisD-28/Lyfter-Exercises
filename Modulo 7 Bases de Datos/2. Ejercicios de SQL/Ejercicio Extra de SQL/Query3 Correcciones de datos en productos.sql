-- SQLite

-- Update para el stock de productos
UPDATE products SET stock_available = 0 WHERE price <= 0;

-- Update para el precio de productos con bajo stock
UPDATE products SET price = price + 100 WHERE stock_available < 10;

-- Update para reducir el stock del producto con ID 1
UPDATE products SET stock_available = stock_available - 1 WHERE product_id = 1;

-- verificar los cambios realizados
SELECT * FROM products ORDER BY id ASC LIMIT 10;