DO $$
DECLARE
    v_user_id INT := 1;        -- Usuario que compra
    v_product_id INT := 1;     -- Producto comprado
    v_quantity INT := 2;       -- Cantidad comprada

    v_stock INT;
    v_price NUMERIC;
    v_bill_id INT;

BEGIN
    -- 1. verificar que el usuario existe
    PERFORM 1 FROM ejercicios_transacciones.Users WHERE user_id = v_user_id;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'El usuario % no existe', v_user_id;
    END IF;

    -- 2. verificar producto y stock
    SELECT stock, price INTO v_stock, v_price
    FROM ejercicios_transacciones.Products
    WHERE product_id = v_product_id;

    IF v_stock IS NULL THEN
        RAISE EXCEPTION 'EL producto % no existe', v_product_id;
    END IF;

    -- 3. Crear factura
    INSERT INTO ejercicios_transacciones.Bills (user_id, total)
    VALUES (v_user_id, v_quantity * v_price)
    RETURNING bill_id INTO v_bill_id;

    -- 4. Insertar detalle
    INSERT INTO ejercicios_transacciones.BillProducts (bill_id, product_id, quantity, subtotal) 
    VALUES (v_bill_id, v_product_id, v_quantity, v_quantity * v_price);

    -- 5. Reducir stock
    UPDATE ejercicios_transacciones.Products
    SET stock = stock - v_quantity
    WHERE product_id = v_product_id;

    RAISE NOTICE 'Compra realizada exitosamente. Factura ID: %', v_bill_id;

END $$;

