from students.validators import *
from students.actions import add_student
import csv
import os

def export_students_to_csv(students):
    while True:
        if not students:
            option = menu_empty_students_list()
            if option == 'back':
                return students
            elif option == 'add':
                add_student(students)
        else:
            subjects = set()
            for estudent in students:
                subjects.update(estudent['grades'].keys())
            subjects = sorted(subjects)

            headers = ['Student full name', 'Group'] + [f'{subject.capitalize()} grade' for subject in subjects]

            # file_exists = os.path.isfile('students.csv')
            # empty_file = False

            # if file_exists:
            #     empty_file = os.path.getsize('students.csv') == 0

            with open('students.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                # if not file_exists or empty_file:
                #     writer.writeheader()

                for student in students:
                    row = {
                        'Student full name': student['name'],
                        'Group': student['group']
                    }
                    for subject in subjects:
                        row[f'{subject.capitalize()} grade'] = student['grades'].get(subject, '')
                    writer.writerow(row)
            
            print('\nStudents data exported successfully to students.csv and the actual students list has been cleared.')
            print('\nType "back" to return to main menu')
            valid_options = ('back',)
            while True:
                option = input('Enter your option: ').strip().lower()

                if option in valid_options:
                    students.clear()
                    return 
                
                print('Invalid input. Please enter "back" to go back to the main menu.')


def import_students_csv(students):
    while True:
        if not os.path.isfile('students.csv'):
            print('\nNo students.csv file found. Please export students data to a CSV file first.')
            print('\nType "back" to return to the main menu or "add" to add a student.')
            valid_options = ('back')
            while True:
                option = input('Enter your option: ').strip().lower()

                if option == 'back':
                    return students
                print('Invalid input. Please enter "back" to go back to the main menu.')

        
        with open('students.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    'name': row['Student full name'],
                    'group': row['Group'],
                    'grades': {
                        'spanish': float(row.get('Spanish grade', 0)),
                        'english': float(row.get('English grade', 0)),
                        'socials': float(row.get('Socials grade', 0)),
                        'science': float(row.get('Science grade', 0))
                    }
                }
                students.append(student)

        print('\nStudents data imported successfully from students.csv')
        print('Type "back" to return to main menu')
        valid_options = ('back',)
        while True:
            option = input('Enter your option: ').strip().lower()

            if option in valid_options:
                return students
            
            print('Invalid input. Please enter "back" to go back to the main menu.')




