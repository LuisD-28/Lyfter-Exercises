-- Ejercicio de normalización: Hospital & Citas Médicas

-- Tabla original sin normalizar
-- CREATE TABLE AppointmentsRaw (
--     appointment_id TEXT,
--     patient_name TEXT,
--     patient_phone TEXT,
--     doctor_name TEXT,
--     specialty TEXT,
--     appointment_date DATE,
--     appointment_time TEXT
-- );

select * from AppointmentsRaw;

-- Paso 1: primera forma normal (1FN)
-- Problema: En teoria la tabla ya cumple con la 1FN, pero prensenta redundancia innecesaria que afecta 2FN y 3FN.
-- Solución: Appointments_1FN, para documentar mejor el proceso.

-- Tabla Appointments_1FN
-- CREATE TABLE Appointments_1FN (
--     appointment_id TEXT,
--     patient_name TEXT,
--     patient_phone TEXT,
--     doctor_name TEXT,
--     specialty TEXT,
--     appointment_date DATE,
--     appointment_time TEXT
-- );

select * from Appointments_1FN;

-- Paso 2: Segunda forma normal (2FN)
-- Problema: La tabla mezcla tres entidades diferentes (citas, pacientes y doctores) lo que genera dependencias parciales
-- Solución: Separar las entidades en tablas diferentes (Patients, Doctors, Appointments).

-- Tabla Patients_2FN
-- CREATE TABLE Patients_2FN (
--     patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     patient_name TEXT NOT NULL,
--     patient_phone TEXT NOT NULL
-- );

-- Tabla Doctors_2FN
-- CREATE TABLE Doctors_2FN (
--     doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     doctor_name TEXT NOT NULL,
--     specialty TEXT NOT NULL
-- );

-- Tabla Appointments_2FN
-- CREATE TABLE Appointments_2FN (
--     appointment_id TEXT PRIMARY KEY,
--     patient_id INTEGER NOT NULL,
--     doctor_id INTEGER NOT NULL,
--     appointment_date DATE NOT NULL,
--     appointment_time TEXT NOT NULL,
--     FOREIGN KEY (patient_id) REFERENCES Patients_2FN(patient_id),
--     FOREIGN KEY (doctor_id) REFERENCES Doctors_2FN(doctor_id)
-- );

select * from Patients_2FN;
select * from Doctors_2FN;
select * from Appointments_2FN;

-- Paso 3: Tercera forma normal (3FN)
-- Problema: Speciality no deberia depender directamente de la clave primaria doctor_id
-- Solución: Crear una tabla separada para las especialidades y eliminar la información de especialidad de la tabla Doctors.

-- Tabla Specialties_3FN
-- CREATE TABLE Specialties_3FN (
--     specialty_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     specialty_name TEXT NOT NULL
-- );

-- Tabla Doctors_3FN
-- CREATE TABLE Doctors_3FN (
--     doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     doctor_name TEXT NOT NULL,
--     specialty_id INTEGER NOT NULL,
--     FOREIGN KEY (specialty_id) REFERENCES Specialties_3FN(specialty_id)
-- );

-- Tabla Patients_3FN(sin cambios respecto a 2FN)
-- CREATE TABLE Patients_3FN (
--     patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     patient_name TEXT NOT NULL,
--     patient_phone TEXT NOT NULL
-- );

-- Tabla Appointments_3FN(sin cambios respecto a 2FN)
-- CREATE TABLE Appointments_3FN (
--     appointment_id TEXT PRIMARY KEY,
--     patient_id INTEGER NOT NULL,
--     doctor_id INTEGER NOT NULL,
--     appointment_date DATE NOT NULL,
--     appointment_time TEXT NOT NULL,
--     FOREIGN KEY (patient_id) REFERENCES Patients_3FN(patient_id),
--     FOREIGN KEY (doctor_id) REFERENCES Doctors_3FN(doctor_id)
-- );

select * from Specialties_3FN;
select * from Doctors_3FN;
select * from Patients_3FN;
select * from Appointments_3FN;

