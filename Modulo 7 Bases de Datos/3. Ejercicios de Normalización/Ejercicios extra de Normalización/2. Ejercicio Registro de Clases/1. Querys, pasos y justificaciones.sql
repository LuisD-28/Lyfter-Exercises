-- Ejercicio de normalización: Registro de Clases

-- Tabla original sin normalizar
-- CREATE TABLE ClassRegistrationRaw (
--     student_id INTEGER,
--     student_name TEXT,
--     course_code TEXT,
--     course_name TEXT,
--     instructor_name TEXT,
--     instructor_email TEXT
-- );

select * from ClassRegistrationRaw;

-- Paso 1: Primera forma normal (1FN)
-- Problema: Redundancia innecesaria y datos repetidos, los datos del curso e instructor se repiten por cada estudiante registrado.
--           La tabla mezcla varias entidades (estudiantes, cursos, instructores) en una sola tabla, lo que generara conflictos para la 2FN y 3FN.
-- Solución: En teoria la tabla ya cumple con la 1FN, pero para documentar mejor el proceso, renombraremos la tabla a ClassRegistration_1FN.

-- Tabla ClassRegistration_1FN
-- CREATE TABLE ClassRegistration_1FN (
--     student_id INTEGER,
--     student_name TEXT,
--     course_code TEXT,
--     course_name TEXT,
--     instructor_name TEXT,
--     instructor_email TEXT
-- );

select * from ClassRegistration_1FN;

-- Paso 2: Segunda forma normal (2FN)
-- Problema: Dependecias parciales, atributos que dependen solo de student_id o de course_code, estos atributos no dependen 
--           completamente de la clave primaria compuesta (student_id, course_code).
-- Solución: Separar las entidades que dependan de cada clave primaria en tablas diferentes(Students, Courses, Instructors).

-- Tabla Students_2FN
-- CREATE TABLE Students_2FN (
--     student_id INTEGER PRIMARY KEY,
--     student_name TEXT NOT NULL
-- );

-- Tabla Courses_2FN
-- CREATE TABLE Courses_2FN (
--     course_code TEXT PRIMARY KEY,
--     course_name TEXT NOT NULL,
--     instructor_name TEXT NOT NULL,
--     instructor_email TEXT NOT NULL
-- );

-- Tabla StudentCourses_2FN
-- CREATE TABLE StudentCourses_2FN (
--     student_id INTEGER NOT NULL,
--     course_code TEXT NOT NULL,
--     PRIMARY KEY (student_id, course_code),
--     FOREIGN KEY (student_id) REFERENCES Students_2FN(student_id),
--     FOREIGN KEY (course_code) REFERENCES Courses_2FN(course_code)
-- );

select * from Students_2FN;
select * from Courses_2FN;
select * from StudentCourses_2FN;

-- Paso 3: Tercera forma normal (3FN)
-- Problema: Dependencias transitivas, instructor_name e instructor_email dependen de course_code, pero no dependen directamente de la clave primaria compuesta (student_id, course_code).
-- Solución: Crear una tabla separada para los instructores y eliminar la información del instructor de la tabla Courses.

-- Tabla Instructors_3FN
-- CREATE TABLE Instructors_3FN (
--     instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     instructor_name TEXT NOT NULL,
--     instructor_email TEXT NOT NULL UNIQUE
-- );

-- Tabla Courses_3FN
-- CREATE TABLE Courses_3FN (
--     course_code TEXT PRIMARY KEY,
--     course_name TEXT NOT NULL,
--     instructor_id INTEGER NOT NULL,
--     FOREIGN KEY (instructor_id) REFERENCES Instructors_3FN(instructor_id)
-- );

-- Tabla Students_3FN(ya no cambia)
-- CREATE TABLE Students_3FN (
--     student_id INTEGER PRIMARY KEY,
--     student_name TEXT NOT NULL
-- );

-- Tabla StudentCourses_3FN(ya no cambia)
-- CREATE TABLE StudentCourses_3FN (
--     student_id INTEGER NOT NULL,
--     course_code TEXT NOT NULL,
--     PRIMARY KEY (student_id, course_code),
--     FOREIGN KEY (student_id) REFERENCES Students_3FN(student_id),
--     FOREIGN KEY (course_code) REFERENCES Courses_3FN(course_code)
-- );

-- Ahora nungun atributo no clave depende de otro atributo no clave, y todas las tablas están en 3FN.


select * from Courses_3FN;
select * from Instructors_3FN;
select * from Students_3FN;
select * from StudentCourses_3FN;
