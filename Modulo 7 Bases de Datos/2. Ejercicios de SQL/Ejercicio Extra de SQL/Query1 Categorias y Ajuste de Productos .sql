-- SQLite
-- CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, description TEXT);

-- SELECT * from categories;

-- ALTER TABLE products ADD COLUMN category_id INTEGER;

-- INSERT INTO categories (name, description)
-- VALUES
-- ('Electrónica', 'Dispositivos electrónicos y tecnología'),
-- ('Muebles', 'Artículos para hogar y oficina'),
-- ('Periféricos', 'Accesorios y dispositivos complementarios');

-- SELECT * from categories;

-- UPDATE products SET category_id = 3 WHERE product_id = 1;  -- Teclado -> Periféricos
-- UPDATE products SET category_id = 3 WHERE product_id = 2;  -- Mouse -> Periféricos
-- UPDATE products SET category_id = 1 WHERE product_id = 3;  -- Monitor -> Electrónica
-- UPDATE products SET category_id = 2 WHERE product_id = 4;  -- Silla -> Muebles
-- UPDATE products SET category_id = 3 WHERE product_id = 5;  -- Webcam -> Periféricos

-- SELECT * from products;

-- SELECT product_id, name, price, category_id, stock_available FROM products;