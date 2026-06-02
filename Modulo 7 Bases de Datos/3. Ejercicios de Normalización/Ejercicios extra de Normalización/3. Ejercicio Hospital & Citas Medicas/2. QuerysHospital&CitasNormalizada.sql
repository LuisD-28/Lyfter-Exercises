-- Ejercicio de Normalización: Hospital y Citas Médicas

-- CREATE TABLE Specialties (
--     specialty_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     specialty_name TEXT NOT NULL
-- );

-- CREATE TABLE Doctors (
--     doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     doctor_name TEXT NOT NULL,
--     specialty_id INTEGER NOT NULL,
--     FOREIGN KEY (specialty_id) REFERENCES Specialties(specialty_id)
-- );

-- CREATE TABLE Patients (
--     patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     patient_name TEXT NOT NULL,
--     patient_phone TEXT NOT NULL
-- );

-- CREATE TABLE Appointments (
--     appointment_id TEXT PRIMARY KEY,
--     patient_id INTEGER NOT NULL,
--     doctor_id INTEGER NOT NULL,
--     appointment_date DATE NOT NULL,
--     appointment_time TEXT NOT NULL,
--     FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
--     FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
-- );


select * from Specialties;
select * from Doctors;
select * from Patients;
select * from Appointments;

SELECT appointment_id
FROM Appointments
WHERE patient_id = (
    SELECT patient_id
    FROM Patients
    WHERE patient_name = 'Diana Vargas'
);

SELECT patient_name
FROM Patients
WHERE patient_id = (
    SELECT patient_id
    FROM Appointments
    WHERE appointment_id = 'A01'
);
