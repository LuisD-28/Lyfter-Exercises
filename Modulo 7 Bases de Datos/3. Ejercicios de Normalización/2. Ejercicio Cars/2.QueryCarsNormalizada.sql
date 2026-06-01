--Ejercicio Cars para CarsFinalVersion1.1.db

-- CREATE TABLE CarModels (
--     model_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     make TEXT NOT NULL,
--     model TEXT NOT NULL,
--     year INTEGER NOT NULL,
--     color TEXT NOT NULL
-- );


-- CREATE TABLE Cars (
--     vin TEXT PRIMARY KEY,
--     model_id INTEGER NOT NULL,
--     FOREIGN KEY (model_id) REFERENCES CarModels(model_id)
-- );


-- CREATE TABLE Owners (
--     owner_id INTEGER PRIMARY KEY,
--     owner_name TEXT NOT NULL,
--     owner_phone TEXT NOT NULL
-- );


-- CREATE TABLE OwnersCars (
--     vin TEXT NOT NULL,
--     owner_id INTEGER NOT NULL,
--     PRIMARY KEY (vin, owner_id),
--     FOREIGN KEY (vin) REFERENCES Cars(vin),
--     FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
-- );


-- CREATE TABLE InsuranceCompany (
--     company_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company_name TEXT NOT NULL
-- );


-- CREATE TABLE InsurancePolicy (
--     policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company_id INTEGER NOT NULL,
--     policy_name TEXT NOT NULL,
--     FOREIGN KEY (company_id) REFERENCES InsuranceCompany(company_id)
-- );


-- CREATE TABLE Insurance (
--     owner_id INTEGER NOT NULL,
--     policy_id INTEGER NOT NULL,
--     FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
--     FOREIGN KEY (policy_id) REFERENCES InsurancePolicy(policy_id)
-- );

SELECT vin
FROM OwnersCars
WHERE owner_id = (
    SELECT owner_id
    FROM Owners
    WHERE owner_name = 'Alice'
);




-- INSERT INTO CarModels (make, model, year, color)
-- VALUES ('Suzuki', 'Fronx', 2024, 'White');

select * from CarModels;

-- INSERT INTO Cars (vin, model_id) VALUES
-- ('FRONX000001', 4),
-- ('FRONX000002', 4),
-- ('FRONX000003', 4),
-- ('FRONX000004', 4),
-- ('FRONX000005', 4);


select * from Cars;

select * from OwnersCars;