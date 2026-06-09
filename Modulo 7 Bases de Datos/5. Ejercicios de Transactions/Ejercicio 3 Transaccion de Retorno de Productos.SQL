DO $$
DECLARE
    v_bill_id INT := 1;        -- Factura a retornar
    v_product_id INT := 1;     -- Producto devuelto
    v_quantity INT := 2;       -- Cantidad devuelta

    v_exists INT;
    v_original_quantity INT;
BEGIN
    -- 1. Verificar que la factura existe
    SELECT 1 INTO v_exists
    FROM ejercicios_transacciones.Bills
    WHERE bill_id = v_bill_id;

    IF v_exists IS NULL THEN
        RAISE EXCEPTION 'La factura % no existe', v_bill_id;
    END IF;

    -- 2. Verificar que el producto está en la factura
    SELECT quantity INTO v_original_quantity
    FROM ejercicios_transacciones.BillProducts
    WHERE bill_id = v_bill_id
    AND product_id = v_product_id;

    IF v_original_quantity IS NULL THEN
        RAISE EXCEPTION 'El producto % no pertenece a la factura %',
            v_product_id, v_bill_id;
    END IF;

    -- 3. Aumentar stock del producto
    UPDATE ejercicios_transacciones.Products
    SET stock = stock + v_quantity
    WHERE product_id = v_product_id;

    -- 4. Marcar factura como "Retornada"
    UPDATE ejercicios_transacciones.Bills
    SET total = 0,
        bill_date = NOW()
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura % marcada como Retornada y stock actualizado', v_bill_id;

END $$;
