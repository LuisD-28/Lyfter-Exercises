-- Ejercicio Cars para Cars.db

-- CREATE TABLE CarsRaw (
--     vin TEXT,
--     make TEXT,
--     model TEXT,
--     year INTEGER,
--     color TEXT,
--     owner_id INTEGER,
--     owner_name TEXT,
--     owner_phone TEXT,
--     insurance_company TEXT,
--     insurance_policy TEXT
-- );

-- INSERT INTO CarsRaw VALUES
-- ('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 101, 'Alice', '123-456-7890', 'ABC Insurance', 'Fire & Theft'),
-- ('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 102, 'Bob', '987-654-3210', 'XYZ Insurance', 'Full Cover'),
-- ('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue', 103, 'Claire', '555-123-4567', 'DEF Insurance', 'Collision'),
-- ('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red', 104, 'Dave', '111-222-3333', 'GHI Insurance', 'Basic Legal');

select * from CarsRaw;

-- Problemas detectados:

-- 1. Mezcla de multiples entidades en una sola tabla, lo que dificulta la gestion y el mantenimiento de los datos.
-- 2. No existe una clave primaria clara que identifique de manera unica cada registro.
-- 3. Dependencias parciales, parte de la información depende solo de una parte de la clave compuesta (vin, owner_id).
-- 4. Dependencias transitivas, la informacion esta mezclada entre el auto, el propietario y el seguro.
-- 5. Redundancia de datos, repeticion innecesaria de datos como el caso del vin '1HGCM82633A' que se repite dos veces con diferente propietario y seguro.

-- Paso 1 - Primera Forma Normal (1FN)
-- No debe haber valores repetidos, ni grupos de datos relacionados.
-- Cada fila debe ser unica y representar una entidad.

-- Problema: Un mismo auto aparece con diferente propietario y seguro, ademas de mezclar multiples entidades.
-- Solución: Seprar la tabla en dos, tablas Cars y Owners.

-- Tabla Cars_1FN
-- CREATE TABLE Cars_1FN (
--     vin TEXT PRIMARY KEY,
--     make TEXT,
--     model TEXT,
--     year INTEGER,
--     color TEXT
-- );

-- Tabla Owners_1FN
-- CREATE TABLE OwnersCars_1FN (
--     vin TEXT,
--     owner_id INTEGER,
--     owner_name TEXT,
--     owner_phone TEXT,
--     insurance_company TEXT,
--     insurance_policy TEXT
-- );

-- INSERT INTO Cars_1FN VALUES
-- ('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver'),
-- ('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue'),
-- ('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');

-- INSERT INTO OwnersCars_1FN VALUES
-- ('1HGCM82633A', 101, 'Alice', '123-456-7890', 'ABC Insurance', 'Fire & Theft'),
-- ('1HGCM82633A', 102, 'Bob', '987-654-3210', 'XYZ Insurance', 'Full Cover'),
-- ('5J6RM4H79EL', 103, 'Claire', '555-123-4567', 'DEF Insurance', 'Collision'),
-- ('1G1RA6EH1FU', 104, 'Dave', '111-222-3333', 'GHI Insurance', 'Basic Legal');

select * from Cars_1FN;
select * from OwnersCars_1FN;

-- Paso 2 - Segunda Forma Normal (2FN)
-- No debe haber dependencias parciales, eliminar campos que no dependan de la clave primaria.
-- Si la clave primaria es compuesta, ningún atributo no clave puede depender solo de una parte de la clave.

-- Problema: La tabla OwnersCars_1FN tiene como clave compuesta (vin, owner_id) lo que sifnifica que los datos del propietario y
--           y del seguro dependen solo del owner_id y no del vin.
-- Solución: Separar las entidades(Owners e Insurance).

-- Tabla Owners
-- CREATE TABLE Owners (
--     owner_id INTEGER PRIMARY KEY,
--     owner_name TEXT,
--     owner_phone TEXT
-- );

-- Tabla Insurance
-- CREATE TABLE Insurance (
--     owner_id INTEGER,
--     insurance_company TEXT,
--     insurance_policy TEXT
-- );

-- Tabla OwnersCars_2FN
-- CREATE TABLE OwnersCars_2FN (
--     vin TEXT,
--     owner_id INTEGER
-- );

-- INSERT INTO Owners VALUES
-- (101, 'Alice', '123-456-7890'),
-- (102, 'Bob', '987-654-3210'),
-- (103, 'Claire', '555-123-4567'),
-- (104, 'Dave', '111-222-3333');

-- INSERT INTO Insurance VALUES
-- (101, 'ABC Insurance', 'Fire & Theft'),
-- (102, 'XYZ Insurance', 'Full Cover'),
-- (103, 'DEF Insurance', 'Collision'),
-- (104, 'GHI Insurance', 'Basic Legal');

-- INSERT INTO OwnersCars_2FN VALUES
-- ('1HGCM82633A', 101),
-- ('1HGCM82633A', 102),
-- ('5J6RM4H79EL', 103),
-- ('1G1RA6EH1FU', 104);

select * from Owners;
select * from Insurance;
select * from OwnersCars_2FN;

-- Paso 3 - Tercera Forma Normal (3FN)
-- No debe haber dependencias transitivas, eliminar campos que dependan de otros campos no clave.
-- Una columna no clave no puede depender de otra columna no clave.

-- Problema: Dependecias transitivas, en Insurance el owner_id es la clave primaria pero insurance_company e insurance_policy dependen del propietario no del seguro.
-- Solución: Separar la entidad InsuranceCompany.

-- Tabla InsuranceCompany
-- CREATE TABLE InsuranceCompany (
--     insurance_company TEXT PRIMARY KEY,
--     insurance_policy TEXT
-- );

-- Tabla Insurance_3FN
-- CREATE TABLE Insurance_3FN (
--     owner_id INTEGER,
--     insurance_company TEXT,
--     FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
--     FOREIGN KEY (insurance_company) REFERENCES InsuranceCompany(insurance_company)
-- );

-- INSERT INTO InsuranceCompany VALUES
-- ('ABC Insurance', 'Fire & Theft'),
-- ('XYZ Insurance', 'Full Cover'),
-- ('DEF Insurance', 'Collision'),
-- ('GHI Insurance', 'Basic Legal');

-- INSERT INTO Insurance_3FN VALUES
-- (101, 'ABC Insurance'),
-- (102, 'XYZ Insurance'),
-- (103, 'DEF Insurance'),
-- (104, 'GHI Insurance');


select * from InsuranceCompany;
select * from Insurance_3FN;

-- Con esto tenemos tablas sin redundancia, sin dependencias parciales ni transitivas, cada tabla representa una entidad y los datos estan organizados de manera eficiente.