-- CREATE SCHEMA EJERCICIOS_TRANSACCIONES;

-- Tabla Users
CREATE TABLE ejercicios_transacciones.Users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla Products
CREATE TABLE ejercicios_transacciones.Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL CHECK (price > 0),
    stock INT NOT NULL CHECK (stock >= 0),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla Bills
CREATE TABLE ejercicios_transacciones.Bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    bill_date TIMESTAMP DEFAULT NOW(),
    total NUMERIC(12,2) DEFAULT 0 CHECK (total >= 0),

    CONSTRAINT fk_bill_user
        FOREIGN KEY (user_id) REFERENCES ejercicios_transacciones.Users(user_id)
);

-- Tabla Bill Products
CREATE TABLE ejercicios_transacciones.BillProducts (
    bill_product_id SERIAL PRIMARY KEY,
    bill_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    subtotal NUMERIC(12,2) NOT NULL CHECK (subtotal >= 0),

    CONSTRAINT fk_bill
        FOREIGN KEY (bill_id) REFERENCES ejercicios_transacciones.Bills(bill_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id) REFERENCES ejercicios_transacciones.Products(product_id)
);

-- Columna status en Bills
ALTER TABLE ejercicios_transacciones.Bills
ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'Completada';



