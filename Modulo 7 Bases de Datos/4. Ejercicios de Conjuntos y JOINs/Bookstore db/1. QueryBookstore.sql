-- CREATE TABLE Authors (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL
-- );

-- CREATE TABLE Books (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     author_id INTEGER,
--     FOREIGN KEY (author_id) REFERENCES Authors(id)
-- );

-- CREATE TABLE Customers (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     email TEXT NOT NULL
-- );

-- CREATE TABLE Rents (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     book_id INTEGER NOT NULL,
--     customer_id INTEGER NOT NULL,
--     state TEXT NOT NULL,
--     FOREIGN KEY (book_id) REFERENCES Books(id),
--     FOREIGN KEY (customer_id) REFERENCES Customers(id)
-- );

-- 1. Obtenga todos los libros y sus autores (en caso de tenerlos):
SELECT Books.name AS book,
        Authors.name AS author
FROM Books
LEFT JOIN Authors ON Books.author_id = Authors.id;

-- 2. Obtenga todos los libros que no tienen autor:
SELECT name
FROM Books
WHERE author_id IS NULL;

-- 3. Obtenga todos los autores que no tienen libros:
SELECT Authors.name
FROM Authors
LEFT JOIN Books
    ON Books.author_id = Authors.id
WHERE Books.id IS NULL;

-- 4. Obtenga todos los libros que han sido rentados en algún momento:
SELECT DISTINCT Books.name -- DISTINCT evita que un libro aparezca repetido si fue rentado varias veces.
FROM Books
INNER JOIN Rents
    ON Books.id = Rents.book_id;

-- 5. Obtenga todos los libros que nunca han sido rentados:
SELECT Books.name
FROM Books
LEFT JOIN Rents
    ON Books.id = Rents.book_id
WHERE Rents.id IS NULL;

-- 6. Obtenga todos los clientes que nunca han rentado un libro:
SELECT Customers.name
FROM Customers
LEFT JOIN Rents
    ON Rents.customer_id = Customers.id
WHERE Rents.id IS NULL;

-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”:
SELECT Books.name AS book,
        Customers.name AS customer,
        Rents.state
FROM Rents
INNER JOIN Books
    ON Rents.book_id = Books.id
INNER JOIN Customers
    ON Rents.customer_id = Customers.id
WHERE Rents.state = 'Overdue';
