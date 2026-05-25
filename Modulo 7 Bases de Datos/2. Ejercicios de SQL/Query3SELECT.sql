-- SQLite

-- 1. todos los productos
select * from products;

-- 2. productos con precio mayor a 50000
select * from products where price > 50000;

-- 3. todas las compras de un mismo producto por id
SELECT invoice_id, quantity, total_amount
FROM InvoiceProducts
WHERE product_id = 1;

-- 4. total de compras por producto y total comprado entre todos las compras
SELECT 
    product_id,
    SUM(quantity) AS total_comprado
FROM InvoiceProducts
GROUP BY product_id;

-- 5. total de facturas por comprador
SELECT * FROM Invoices WHERE user_id = 1;

-- 6. total de facturas ordenadas por monto total de forma descendente
SELECT * FROM Invoices ORDER BY total_amount DESC;

-- 7. factura por numero de factura
SELECT * FROM Invoices WHERE invoice_number = 'FAC-001';