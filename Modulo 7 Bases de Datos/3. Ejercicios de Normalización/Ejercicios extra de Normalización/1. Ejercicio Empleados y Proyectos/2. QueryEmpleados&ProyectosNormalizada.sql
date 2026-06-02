-- CREATE TABLE Departments (
--     department_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     department_name TEXT NOT NULL,
--     department_phone TEXT NOT NULL
-- );

-- CREATE TABLE Employees (
--     employee_id INTEGER PRIMARY KEY,
--     employee_name TEXT NOT NULL,
--     department_id INTEGER NOT NULL,
--     FOREIGN KEY (department_id) REFERENCES Departments(department_id)
-- );

-- CREATE TABLE Projects (
--     project_id TEXT PRIMARY KEY,
--     project_name TEXT NOT NULL,
--     project_budget INTEGER NOT NULL
-- );

-- CREATE TABLE EmployeeProjects (
--     employee_id INTEGER NOT NULL,
--     project_id TEXT NOT NULL,
--     PRIMARY KEY (employee_id, project_id),
--     FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
--     FOREIGN KEY (project_id) REFERENCES Projects(project_id)
-- );


select * from Departments;
select * from Employees;
select * from Projects;
select * from EmployeeProjects;

SELECT project_id
FROM EmployeeProjects
WHERE employee_id = (
    SELECT employee_id
    FROM Employees
    WHERE employee_name = 'Ana Rivera'
);

SELECT employee_name
FROM Employees
WHERE employee_id IN (
    SELECT employee_id
    FROM EmployeeProjects
    WHERE project_id = 'P001'
);


