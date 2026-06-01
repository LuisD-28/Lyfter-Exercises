-- PRAGMA foreign_keys = ON;

-- CREATE TABLE Customers (
--     customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     customer_name TEXT NOT NULL,
--     customer_phone TEXT NOT NULL,
--     address TEXT NOT NULL
-- );

-- CREATE TABLE Orders (
--     order_id TEXT PRIMARY KEY,
--     customer_id INTEGER NOT NULL,
--     delivery_time TEXT NOT NULL,
--     FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
-- );

-- CREATE TABLE Products (
--     item_id INTEGER PRIMARY KEY,
--     item_name TEXT NOT NULL,
--     price REAL NOT NULL
-- );

-- CREATE TABLE OrderItems (
--     order_id TEXT NOT NULL,
--     item_id INTEGER NOT NULL,
--     quantity INTEGER NOT NULL,
--     special_request TEXT,
--     PRIMARY KEY (order_id, item_id),
--     FOREIGN KEY (order_id) REFERENCES Orders(order_id),
--     FOREIGN KEY (item_id) REFERENCES Products(item_id)
-- );


select * from Customers;

select * from Orders;

select * from Products;

select * from OrderItems;

SELECT order_id, delivery_time
FROM Orders
WHERE customer_id = (
    SELECT customer_id
    FROM Customers
    WHERE customer_name = 'Claire'
);