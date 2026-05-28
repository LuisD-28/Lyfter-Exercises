--Ejercicio Cars para Cars(FinalVersion).db

-- CREATE TABLE Cars (
--     vin TEXT PRIMARY KEY,
--     make TEXT NOT NULL,
--     model TEXT NOT NULL,
--     year INTEGER NOT NULL,
--     color TEXT NOT NULL
-- );

-- CREATE TABLE Owners (
--     owner_id INTEGER PRIMARY KEY,
--     owner_name TEXT NOT NULL,
--     owner_phone TEXT NOT NULL
-- );

-- CREATE TABLE InsuranceCompany (
--     insurance_company TEXT PRIMARY KEY,
--     insurance_policy TEXT NOT NULL
-- );

-- CREATE TABLE Insurance (
--     owner_id INTEGER,
--     insurance_company TEXT,
--     FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
--     FOREIGN KEY (insurance_company) REFERENCES InsuranceCompany(insurance_company)
-- );

-- CREATE TABLE OwnersCars (
--     vin TEXT,
--     owner_id INTEGER,
--     PRIMARY KEY (vin, owner_id),
--     FOREIGN KEY (vin) REFERENCES Cars(vin),
--     FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
-- );

select * from Cars;
select * from Owners;
select * from InsuranceCompany;
select * from Insurance;
select * from OwnersCars;

SELECT vin
FROM OwnersCars
WHERE owner_id = (
    SELECT owner_id
    FROM Owners
    WHERE owner_name = 'Alice'
);

SELECT insurance_policy
FROM InsuranceCompany
WHERE insurance_company = (
    SELECT insurance_company
    FROM Insurance
    WHERE owner_id = 102
);
