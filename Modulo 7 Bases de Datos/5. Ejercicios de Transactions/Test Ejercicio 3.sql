INSERT INTO ejercicios_transacciones.BillProducts (bill_id, product_id, quantity, subtotal)
VALUES (1, 2, 2, 100.00);

select * from ejercicios_transacciones.bills

SELECT *
FROM ejercicios_transacciones.BillProducts
WHERE bill_id = 1;
