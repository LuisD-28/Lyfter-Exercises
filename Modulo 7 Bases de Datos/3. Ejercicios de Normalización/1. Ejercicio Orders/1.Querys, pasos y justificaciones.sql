-- Ejercicio Orders

--     CREATE TABLE OrdersRaw (
--     order_id TEXT,
--     customer_name TEXT,
--     customer_phone TEXT,
--     address TEXT,
--     item_id INTEGER,
--     item_name TEXT,
--     price REAL,
--     quantity INTEGER,
--     special_request TEXT,
--     delivery_time TEXT
-- );
-- INSERT INTO OrdersRaw VALUES
-- ('001', 'Alice', '123-456-7890', '123 Main St', 101, 'Cheeseburger', 8, 2, 'No onions', '6:00 PM'),
-- ('001', 'Alice', '123-456-7890', '123 Main St', 102, 'Fries', 3, 1, 'Extra ketchup', '6:00 PM'),
-- ('002', 'Bob', '987-654-3210', '456 Elm St', 103, 'Pizza', 12, 1, 'Extra cheese', '7:30 PM'),
-- ('002', 'Bob', '987-654-3210', '4th Avenue', 102, 'Fries', 3, 2, 'None', '7:30 PM'),
-- ('003', 'Claire', '555-123-4567', '789 Oak St', 105, 'Salad', 6, 1, 'No croutons', '12:00 PM'),
-- ('004', 'Claire', '555-123-4567', '464 Georgia St', 106, 'Water', 1, 1, 'None', '5:00 PM');

select * from OrdersRaw;

-- Problemas Detectados:

-- 1. Repite datos del cliente.
-- 2. Ordenes duplicadas.
-- 3. Diferentes direcciones para un mismo cliente.
-- 4. La tabla mezcla todo tipo de informacion como ordenes, clientes y productos

-- Paso 1 - Primera Forma Normal (1FN)
-- No debe haber valores repetidos, ni grupos de datos relacionados.
-- Cada fila debe ser unica y representar una entidad.

-- Problema: Una orden con varios productos aparece repetida varias veces(Order 001 y 002)
--           Esto
-- Solución: Separar en dos tablas Orders y OrderItems

-- Tabla Orders_1FN 
-- CREATE TABLE Orders_1FN (
--     order_id TEXT PRIMARY KEY,
--     customer_name TEXT,
--     customer_phone TEXT,
--     address TEXT,
--     delivery_time TEXT
-- );
-- Tabla OrderItems_1FN
-- CREATE TABLE OrderItems_1FN (
--     order_id TEXT,
--     item_id INTEGER,
--     item_name TEXT,
--     price REAL,
--     quantity INTEGER,
--     special_request TEXT
-- );

-- Insert para Orders_1FN
-- INSERT INTO Orders_1FN VALUES
-- ('001', 'Alice', '123-456-7890', '123 Main St', '6:00 PM'),
-- ('002', 'Bob', '987-654-3210', '456 Elm St', '7:30 PM'),
-- ('003', 'Claire', '555-123-4567', '789 Oak St', '12:00 PM'),
-- ('004', 'Claire', '555-123-4567', '464 Georgia St', '5:00 PM');

-- Insert para OrderItems_1FN
-- INSERT INTO OrderItems_1FN VALUES
-- ('001', 101, 'Cheeseburger', 8, 2, 'No onions'),
-- ('001', 102, 'Fries', 3, 1, 'Extra ketchup'),
-- ('002', 103, 'Pizza', 12, 1, 'Extra cheese'),
-- ('002', 102, 'Fries', 3, 2, 'None'),
-- ('003', 105, 'Salad', 6, 1, 'No croutons'),
-- ('004', 106, 'Water', 1, 1, 'None');

select * from Orders_1FN;
select * from OrderItems_1FN;

-- Paso 2 - Segunda Forma Normal (2FN)
-- No debe haber dependencias parciales, eliminar campos que no dependan de la clave primaria.
-- Solo puede ocurrir en tablas donde la llave primaria esta conformada por varias columnas.

-- Problema: En OrderItems_1FN la tabla tine como clave compuesta oirder_id e item_id pero item_name y 
--           price dependen solo de item_id esto va en contra de la 2NF
-- Solución: Separar los datos del producto en una tabla independiente

-- Tabla Products
-- CREATE TABLE Products (
--     item_id INTEGER PRIMARY KEY,
--     item_name TEXT,
--     price REAL
-- );

-- Tabla OrderItems_2FN
-- CREATE TABLE OrderItems_2FN (
--     order_id TEXT,
--     item_id INTEGER,
--     quantity INTEGER,
--     special_request TEXT
-- );

-- Insert para Products
-- INSERT INTO Products VALUES
-- (101, 'Cheeseburger', 8),
-- (102, 'Fries', 3),
-- (103, 'Pizza', 12),
-- (105, 'Salad', 6),
-- (106, 'Water', 1);

-- Insert para OrderItems_2FN
-- INSERT INTO OrderItems_2FN VALUES
-- ('001', 101, 2, 'No onions'),
-- ('001', 102, 1, 'Extra ketchup'),
-- ('002', 103, 1, 'Extra cheese'),
-- ('002', 102, 2, 'None'),
-- ('003', 105, 1, 'No croutons'),
-- ('004', 106, 1, 'None');

select * from Products;
select * from OrderItems_2FN;

--Paso 3 - Tercera Forma Normal (3FN)
-- No existen dependencias transitivas, eliminar campos que dependan de otros campos que no
-- Es decir, una columna no clave no puede depender de otra columna no clave.

-- problema: En la tabla Orders_1FN tiene como clave primaria order_id pero customer_name, customer_phone y address
--           dependen del cliente no de la orden ademas los datos del cliente se repiten, en la tabla original OrdersRaw 
--           el cliente Bob y Claire tienen diferentes direcciones.

-- Solución: Separar los datos del cliente en una tabla independiente.

--Tabla Customers
-- CREATE TABLE Customers (
--     customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     customer_name TEXT,
--     customer_phone TEXT,
--     address TEXT
-- );

-- Tabla Orders_3FN
-- CREATE TABLE Orders_3FN (
--     order_id TEXT PRIMARY KEY,
--     customer_id INTEGER,
--     delivery_time TEXT
-- );

-- INSERT INTO Customers VALUES
-- (1, 'Alice', '123-456-7890', '123 Main St'),
-- (2, 'Bob', '987-654-3210', '456 Elm St'),
-- (3, 'Claire', '555-123-4567', '789 Oak St');

-- INSERT INTO Orders_3FN VALUES
-- ('001', 1, '6:00 PM'),
-- ('002', 2, '7:30 PM'),
-- ('003', 3, '12:00 PM'),
-- ('004', 3, '5:00 PM');

select * from Customers;
select * from Orders_3FN;

--Ahora tenemos cada tabla sin dependencias parciales ni transitivas, cada tabla representa una entidad y no hay datos repetidos.

