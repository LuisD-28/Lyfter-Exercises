DO $$
DECLARE
    v_bill_id INT := 1;

    -- productos devueltos
    v_items JSON := '[
        {"product_id": 1, "quantity": 1},
        {"product_id": 2, "quantity": 2}
    ]';

    rec JSON;
    v_product_id INT;
    v_quantity INT;
    v_original_quantity INT;
BEGIN
    -- 1. Verificar factura
    PERFORM 1 FROM ejercicios_transacciones.Bills WHERE bill_id = v_bill_id;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'La factura % no existe', v_bill_id;
    END IF;

    -- 2. Procesar cada producto devuelto
    FOR rec IN SELECT * FROM json_array_elements(v_items) LOOP
        v_product_id := (rec->>'product_id')::INT;
        v_quantity   := (rec->>'quantity')::INT;

        -- 2.1 Verificar que el producto pertenece a la factura
        SELECT quantity INTO v_original_quantity
        FROM ejercicios_transacciones.BillProducts
        WHERE bill_id = v_bill_id
        AND product_id = v_product_id;

        IF v_original_quantity IS NULL THEN
            RAISE EXCEPTION 'El producto % no pertenece a la factura %',
                v_product_id, v_bill_id;
        END IF;

        -- 2.2 Aumentar stock
        UPDATE ejercicios_transacciones.Products
        SET stock = stock + v_quantity
        WHERE product_id = v_product_id;
    END LOOP;

    -- 3. Marcar factura como retornada
    UPDATE ejercicios_transacciones.Bills
    SET status = 'Retornada', total = 0
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como Retornada y stock actualizado', v_bill_id;

END $$;


-- DO $$
-- DECLARE
--     v_bill_id INT := 1;        -- Factura a retornar
--     v_product_id INT := 1;     -- Producto devuelto
--     v_quantity INT := 2;       -- Cantidad devuelta

--     v_exists INT;
--     v_original_quantity INT;
-- BEGIN
--     -- 1. Verificar que la factura existe
--     SELECT 1 INTO v_exists
--     FROM ejercicios_transacciones.Bills
--     WHERE bill_id = v_bill_id;

--     IF v_exists IS NULL THEN
--         RAISE EXCEPTION 'La factura % no existe', v_bill_id;
--     END IF;

--     -- 2. Verificar que el producto está en la factura
--     SELECT quantity INTO v_original_quantity
--     FROM ejercicios_transacciones.BillProducts
--     WHERE bill_id = v_bill_id
--     AND product_id = v_product_id;

--     IF v_original_quantity IS NULL THEN
--         RAISE EXCEPTION 'El producto % no pertenece a la factura %',
--             v_product_id, v_bill_id;
--     END IF;

--     -- 3. Aumentar stock del producto
--     UPDATE ejercicios_transacciones.Products
--     SET stock = stock + v_quantity
--     WHERE product_id = v_product_id;

--     -- 4. Marcar factura como "Retornada"
--     UPDATE ejercicios_transacciones.Bills
--     SET total = 0,
--         bill_date = NOW()
--     WHERE bill_id = v_bill_id;

--     RAISE NOTICE 'Factura % marcada como Retornada y stock actualizado', v_bill_id;

-- END $$;
