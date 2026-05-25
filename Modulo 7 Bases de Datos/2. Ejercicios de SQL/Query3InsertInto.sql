-- SQLite
-- INSERT INTO Users (full_name, email, registration_date)
-- VALUES
-- ('Luis Dorantes', 'luis@lyfter.com', '2026-05-20'),
-- ('Sebastian Schweinsteiger', 'sebastian@lyfter.com', '2026-05-21'),
-- ('Carles Puyol', 'puyol@lyfter.com', '2026-05-22');

-- select * from users;

-- INSERT INTO PaymentMethods (method_type, bank_name)
-- VALUES
-- ('Tarjeta de crédito', 'Bank of America'),
-- ('Tarjeta de débito', 'Bank of America'),
-- ('Transferencia bancaria', 'Bank of America'),
-- ('Tarjeta de crédito', 'Chase'),
-- ('Tarjeta de débito', 'Chase'),
-- ('Transferencia bancaria', 'Chase'),
-- ('PayPal', NULL),
-- ('Apple Pay', NULL);

-- select * from paymentmethods;

-- INSERT INTO Products (code, name, price, entry_date, brand, stock_available)
-- VALUES
-- ('P001', 'Teclado mecánico', 79.99, '2026-05-10', 'Logitech', 10),
-- ('P002', 'Mouse inalámbrico', 39.99, '2026-05-11', 'Razer', 20),
-- ('P003', 'Monitor 24 pulgadas', 159.99, '2026-05-12', 'Dell', 25),
-- ('P004', 'Silla ergonómica', 199.99, '2026-05-14', 'Secretlab', 5),
-- ('P005', 'Webcam Full HD', 49.99, '2026-05-15', 'Logitech', 30);

-- select * from products;

-- INSERT INTO ShoppingCart (user_id)
-- VALUES
-- (1),   -- carrito de Luis
-- (2),   -- carrito de Sebastian
-- (3);   -- carrito de Carles

-- select * from shoppingcart;

-- INSERT INTO ShoppingCartProducts (cart_id, product_id, quantity)
-- VALUES
-- (1, 1, 1),   -- Luis agrega 1 teclado
-- (1, 2, 2),   -- Luis agrega 2 mouse
-- (1, 3, 1),   -- Luis agrega 1 monitor
-- (2, 3, 1),   -- Sebastian agrega 1 monitor
-- (2, 4, 1),   -- Sebastian agrega 1 silla
-- (2, 2, 1),   -- Sebastian agrega 1 mouse
-- (3, 1, 1);   -- Carles agrega 1 teclado

-- select * from shoppingcartproducts;

-- INSERT INTO Invoices (
--     invoice_number,
--     purchase_date,
--     total_amount,
--     user_id,
--     method_id,
--     buyer_phone,
--     cashier_code
-- )
-- VALUES
-- ('FAC-001', '2026-05-23', 319.96, 1, 1, '512-555-7890', 'EMP-101'),
-- ('FAC-002', '2026-05-23', 399.97, 2, 2, '737-555-1122', 'EMP-102'),
-- ('FAC-003', '2026-05-23', 79.99, 3, 1, '512-555-3344', 'EMP-103');


-- select * from invoices;

-- INSERT INTO InvoiceProducts (invoice_id, product_id, quantity, total_amount)
-- VALUES
-- (1, 1, 1, 79.99),   -- Luis compra 1 teclado
-- (1, 2, 2, 79.98),   -- Luis compra 2 mouse
-- (1, 3, 1, 159.99),  -- Luis compra 1 monitor
-- (2, 3, 1, 159.99),  -- Sebastian compra 1 monitor
-- (2, 4, 1, 199.99),  -- Sebastian compra 1 silla
-- (2, 2, 1, 39.99),   -- Sebastian compra 1 mouse
-- (3, 1, 1, 79.99);   -- Carles compra 1 teclado

-- select * from invoiceproducts;