-- Numero total de veces que cada cliente ha rentado un libro, ordenado de mayor a menor con limite a 3 clientes mas frecuentes.
SELECT Customers.name, COUNT(Rents.id) AS total_rents
FROM Customers
LEFT JOIN Rents ON Rents.customer_id = Customers.id
GROUP BY Customers.id
ORDER BY total_rents DESC
LIMIT 3;

-- Consulta con multiples JOINs

-- INSERT INTO Rents (book_id, customer_id, state)
-- VALUES (5, 1, 'On time');

SELECT Customers.name AS customer,
    Books.name AS book,
    Authors.name AS author,
    Rents.state
FROM Rents
INNER JOIN Customers
    ON Rents.customer_id = Customers.id
INNER JOIN Books
    ON Rents.book_id = Books.id
LEFT JOIN Authors -- LEFT JOIN para incluir libros sin autor registrado
    ON Books.author_id = Authors.id;


select * from Rents;