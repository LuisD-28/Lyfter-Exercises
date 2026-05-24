PRAGMA foreign_keys = ON;

-- 1. USERS
CREATE TABLE Users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, registration_date TEXT NOT NULL);


-- 2. PAYMENT METHODS
CREATE TABLE PaymentMethods (method_id INTEGER PRIMARY KEY AUTOINCREMENT, method_type TEXT NOT NULL, bank_name TEXT);


-- 3. PRODUCTS
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    entry_date TEXT NOT NULL,
    brand TEXT NOT NULL,
    stock_available INTEGER NOT NULL
);


-- 4. SHOPPING CART
CREATE TABLE ShoppingCart (cart_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES Users(user_id));


-- 5. SHOPPING CART PRODUCTS
CREATE TABLE ShoppingCartProducts (
    cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES ShoppingCart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


-- 6. INVOICES
CREATE TABLE Invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT NOT NULL,
    purchase_date TEXT NOT NULL,
    total_amount REAL NOT NULL,
    user_id INTEGER,
    method_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (method_id) REFERENCES PaymentMethods(method_id)
);


-- 7. INVOICE PRODUCTS
CREATE TABLE InvoiceProducts (
    invoice_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


-- 8. REVIEWS
CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    comment TEXT,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    date TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
