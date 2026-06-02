-- Ejercicio de normalización: Empleados y Proyectos

-- Tabla original sin normalizar
-- CREATE TABLE EmployeeProjectsRaw (
--     employee_id INTEGER,
--     employee_name TEXT,
--     department TEXT,
--     department_phone TEXT,
--     project_id TEXT,
--     project_name TEXT,
--     project_budget INTEGER
-- );

select * from EmployeeProjectsRaw;

-- Paso 1: Primera forma normal (1FN)
-- Problema: Redundancia innecesaria y datos repetidos, los datos del proyecto se repiten por cada empleado asignado.
--           La tabla mezcla varias entidades (empleados, departamentos, proyectos) en una sola tabla.

-- Solución: En teoria la tabla ya cumple con la 1FN, pero para documentar mejor el proceso, renombraremos la tabla a EmployeeProjects_1FN

-- Tabla EmployeeProjects_1FN
-- CREATE TABLE EmployeeProjects_1FN (
--     employee_id INTEGER,
--     employee_name TEXT,
--     department TEXT,
--     department_phone TEXT,
--     project_id TEXT,
--     project_name TEXT,
--     project_budget INTEGER
-- );

select * from EmployeeProjects_1FN;

-- Paso 2: Segunda forma normal (2FN)
-- Problema: La tabla 1FN tiene dependencias parciales, atributos que dependen solo del employee_id o del project_id.
--           Esto rompe 2FN, por que estos atributos no dependen completamente de la clave primaria compuesta (employee_id, project_id).

-- Solucion: Separar las entidades que dependan de cada clave primaria en tablas diferentes(Employees, Departments, Projects).

-- Tabla Employees
-- CREATE TABLE Employees_2FN (
--     employee_id INTEGER PRIMARY KEY,
--     employee_name TEXT,
--     department TEXT,
--     department_phone TEXT
-- );

-- Tabla Projects
-- CREATE TABLE Projects_2FN (
--     project_id TEXT PRIMARY KEY,
--     project_name TEXT,
--     project_budget INTEGER
-- );

-- Tabla EmployeeProjects
-- CREATE TABLE EmployeeProjects_2FN (
--     employee_id INTEGER,
--     project_id TEXT,
--     PRIMARY KEY (employee_id, project_id),
--     FOREIGN KEY (employee_id) REFERENCES Employees_2FN(employee_id),
--     FOREIGN KEY (project_id) REFERENCES Projects_2FN(project_id)
-- );

select * from Employees_2FN;
select * from Projects_2FN;
select * from EmployeeProjects_2FN;

-- Paso 3: Tercera forma normal (3FN)
-- Problema: En la tabla Employees_2FN hay una dependenacia(department y department_phone), el telefono del departamento no depende del empleado, sino del departamento.
-- Solucion: Separar la entidad Departaments en una tabla diferente.

-- Tabla Departments
-- CREATE TABLE Departments (
--     department_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     department_name TEXT NOT NULL,
--     department_phone TEXT NOT NULL
-- );

--Tabla Employees(3FN)
-- CREATE TABLE Employees_3FN (
--     employee_id INTEGER PRIMARY KEY,
--     employee_name TEXT NOT NULL,
--     department_id INTEGER NOT NULL,
--     FOREIGN KEY (department_id) REFERENCES Departments(department_id)
-- );

select * from Departments;
select * from Employees_3FN;


-- Todas las tablas están ahora completamente normalizadas hasta 3FN, eliminando redundancias y dependencias innecesarias.