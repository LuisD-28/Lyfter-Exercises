import students.actions as actions
import students.validators as validators
# get_student_name, get_student_group, get_grade, validate_if_students_exist, validate_students_list


def add_student(students):

    while True:
        try:
            name = validators.get_student_name()
            group = validators.get_student_group()
            spanish_grade = validators.get_grade('Spanish')
            english_grade = validators.get_grade('English')
            socials_grade = validators.get_grade('Socials')
            science_grade = validators.get_grade('Science')

        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue

        student = {
            'name': name,
            'group': group,
            'grades': {
                'spanish': spanish_grade,
                'english': english_grade,
                'socials': socials_grade,
                'science': science_grade
            },
        }
        
        if validators.validate_if_students_exist(students, name, group):
            print(f'Student {name} from group {group} already exists. Please enter a different student.')
            continue
        else:
            students.append(student)
            print(f'\nStudent {name} added successfully!')
        

        while True:
            try:
                option = input('Do you want to add another student? (yes/no): ').lower()
                if option not in ('yes','y','no','n'):
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                if option in ('yes','y'):
                    break
                else:
                    return students
            except ValueError as e:
                print(e)
                continue


def delete_student(students):
    name_to_delete = input("Please enter the student's name and group you want to remove (e.g., Raul Cortez Castillo A1): ")
    for student in students:
        if student['name'] + ' ' + student['group'] == name_to_delete:
            print(f'Are you sure you want to delete this student: {name_to_delete}? (yes/no)')
            while True:
                option = input().lower()
                if option in ('yes', 'y'):
                    students.remove(student)
                    print(f'Student {name_to_delete} has been deleted successfully.')
                    return students
                elif option in ('no', 'n'):
                    print('Deletion cancelled.')
                    return students
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue
        else:
                print("******************************************************************")
                print(f'Student {name_to_delete} not found.')
                while True:
                    options = input('Type "back" to return to the main menu or "delete" to try again: ').lower()
                    if options not in ('back','delete'):
                        print('Invalid input.')
                        continue
                    if options == 'back':
                        return students
                    elif options == 'delete':
                        return delete_student(students)


def get_all_students(students):
    while True:
        if not students:
            option = validators.menu_empty_students_list()
            if option == 'back':
                return students
            elif option == 'add':
                actions.add_student(students)
        else:
            print("\n=== All Students ===")
            for student in students:
                print(f"Name: {student['name']}, Group: {student['group']}, Spanish Grade: {student['grades']['spanish']}, English Grade: {student['grades']['english']}, Socials Grade: {student['grades']['socials']}, Science Grade: {student['grades']['science']}")

            option = validators.menu_navigation_students_list()
            if option == 'back':
                return students
            if option == 'delete':
                delete_student(students)
            if option == 'add':
                add_student(students)


def get_top_students(students):
    while True:
        if not students:
            option = validators.menu_empty_students_list()
            if option == 'back':
                return students
            elif option == 'add':
                actions.add_student(students)
        else:        
            
            students_avg = get_students_average(students)

            if len(students_avg) < 3:
                print("\nNot enough students to display the top 3. Please add more students.")

            else:
                #con lambda x: x['average'] estamos diciendo que queremos ordenar la lista de estudiantes por el valor de la clave 'average' en cada diccionario
                students_avg.sort(key=lambda x: x['average'], reverse=True)
                top_students = students_avg[:3]
                print("\n=== Top 3 Students with the Highest Average Grade ===\n")
                for student in top_students:
                    print(f"Name: {student['name']}, Group: {student['group']}, Average Grade: {student['average']}")
                
            option = validators.menu_navigation_students_list()
            if option == 'back':
                return students
            if option == 'delete':
                actions.delete_student(students)
            if option == 'add':
                actions.add_student(students)


def get_failed_students(students):
    while True:
        if not students:
            option = validators.menu_empty_students_list()
            if option == 'back':
                return students
            elif option == 'add':
                actions.add_student(students)
        else:

            print("\n=== Failed Students (Average Grade Below 60 and/or one or more failed subjects) ===")
            failed_students = []
            for student in students:
                name = student['name']
                group = student['group']
                grades = student['grades']

                failed_subjects = {subject: g for subject, g in grades.items() if g < 60}

                avg = sum(grades.values()) / len(grades)

                if len(failed_subjects) >= 1 or avg < 60:
                    failed_students = ", ".join(f"{subject}: {grade}" for subject, grade in failed_subjects.items())
                    print(f"Name: {name}, Group: {group}, Average Grade: {avg}, Failed Subject(s): {failed_students}")

                    # menu_options_students_list(students)
            option = validators.menu_navigation_students_list()
            
            if option == 'back':
                return students
            if option == 'delete':
                actions.delete_student(students)
            if option == 'add':
                actions.add_student(students)


def students_avg(students):
    
    students_avg = get_students_average(students)

    while True:
        if not students:
            option = validators.menu_empty_students_list()
            if option == 'back':
                return students
            elif option == 'add':
                actions.add_student(students)
        else:

            print("\n=== Overall Students Average ===")
            overall_avg = sum(student['average'] for student in students_avg) / len(students_avg)

            print(f"\nOverall Average Grade: {overall_avg:.2f}\n")



            print("Students average ordered by group:")
            for student in sorted(students_avg, key=lambda x: x['group']):
                print(f"Name: {student['name']}, Group: {student['group']}, Average Grade: {student['average']}")


            
            # print("\n=== Grade Average by Student ===")
            # for student in students_avg: 
            #     print(f"Name: {student['name']}, Group: {student['group']}, Average Grade: {student['average']}")
            
            option = validators.menu_navigation_students_list()
            if option == 'back':
                return students
            if option == 'delete':
                actions.delete_student(students)
            if option == 'add':
                actions.add_student(students)



def get_students_average(students):
    students_avg = []
    for student in students:
        avg = (student['grades']['spanish'] + student['grades']['english'] + student['grades']['socials'] + student['grades']['science']) / len(student['grades'])
        students_avg.append({'name': student['name'], 'group': student['group'], 'average': avg})
    
    return students_avg




# def export_students_to_csv(students):
#     while True:
#         if not students:
#             option = validators.menu_empty_students_list()
#             if option == 'back':
#                 return students
#             elif option == 'add':
#                 add_student(students)
#         else:
#             subjects = set()
#             for estudent in students:
#                 subjects.update(estudent['grades'].keys())
#             subjects = sorted(subjects)

#             headers = ['Student full name', 'Group'] + [f'{subject.capitalize()} grade' for subject in subjects]

#             # file_exists = os.path.isfile('students.csv')
#             # empty_file = False

#             # if file_exists:
#             #     empty_file = os.path.getsize('students.csv') == 0

#             with open('students.csv', 'w', newline='', encoding='utf-8') as file:
#                 writer = csv.DictWriter(file, fieldnames=headers)
#                 writer.writeheader()
#                 # if not file_exists or empty_file:
#                 #     writer.writeheader()

#                 for student in students:
#                     row = {
#                         'Student full name': student['name'],
#                         'Group': student['group']
#                     }
#                     for subject in subjects:
#                         row[f'{subject.capitalize()} grade'] = student['grades'].get(subject, '')
#                     writer.writerow(row)
            
#             print('\nStudents data exported successfully to students.csv and the actual students list has been cleared.')
#             print('\nType "back" to return to main menu')
#             valid_options = ('back',)
#             while True:
#                 option = input('Enter your option: ').strip().lower()

#                 if option in valid_options:
#                     students.clear()
#                     return 
                
#                 print('Invalid input. Please enter "back" to go back to the main menu.')


# def import_students_csv(students):
#     while True:
#         if not os.path.isfile('students.csv'):
#             print('\nNo students.csv file found. Please export students data to a CSV file first.')
#             print('\nType "back" to return to the main menu or "add" to add a student.')
#             valid_options = ('back')
#             while True:
#                 option = input('Enter your option: ').strip().lower()

#                 if option == 'back':
#                     return students
#                 print('Invalid input. Please enter "back" to go back to the main menu.')

        
#         with open('students.csv', 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)

#             for row in reader:
#                 student = {
#                     'name': row['Student full name'],
#                     'group': row['Group'],
#                     'grades': {
#                         'spanish': float(row.get('Spanish grade', 0)),
#                         'english': float(row.get('English grade', 0)),
#                         'socials': float(row.get('Socials grade', 0)),
#                         'science': float(row.get('Science grade', 0))
#                     }
#                 }
#                 students.append(student)

#         print('\nStudents data imported successfully from students.csv')
#         print('Type "back" to return to main menu')
#         valid_options = ('back',)
#         while True:
#             option = input('Enter your option: ').strip().lower()

#             if option in valid_options:
#                 return students
            
#             print('Invalid input. Please enter "back" to go back to the main menu.')





