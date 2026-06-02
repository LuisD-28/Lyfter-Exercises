-- Ejercicio: Registro de Clases Normalizada

-- CREATE TABLE Instructors (
--     instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     instructor_name TEXT NOT NULL,
--     instructor_email TEXT NOT NULL UNIQUE
-- );

-- CREATE TABLE Courses (
--     course_code TEXT PRIMARY KEY,
--     course_name TEXT NOT NULL,
--     instructor_id INTEGER NOT NULL,
--     FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
-- );

-- CREATE TABLE Students (
--     student_id INTEGER PRIMARY KEY,
--     student_name TEXT NOT NULL
-- );

-- CREATE TABLE StudentCourses (
--     student_id INTEGER NOT NULL,
--     course_code TEXT NOT NULL,
--     PRIMARY KEY (student_id, course_code),
--     FOREIGN KEY (student_id) REFERENCES Students(student_id),
--     FOREIGN KEY (course_code) REFERENCES Courses(course_code)
-- );

select * from Instructors;
select * from Courses;
select * from Students;
select * from StudentCourses;


SELECT course_name
FROM Courses
WHERE course_code = 'CS101';

SELECT student_name
FROM Students
WHERE student_id IN (
    SELECT student_id
    FROM StudentCourses
    WHERE course_code = 'CS101'
);