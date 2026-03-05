from students import actions

def get_student_name():
    while True:
        name = input("Please enter the student's full Name: ").strip()
        parts = name.split()
        
        if not name:
            print("Invalid input. Please enter a valid name.")
            continue
        if not all(x.isalpha() or x.isspace() for x in name):
            print("Invalid input. Please enter a valid name.")
            continue
        if len(parts) < 2:
            print("Invalid input. Please enter the full name (at least first name and last name).")
            continue
        
        return name
    

def get_student_group():
    while True:
        group = input("Please enter the student's group: (e.g., 3A, 1B): ").strip()
        
        if not group:
            print("Invalid input. Please enter a valid group.")
            continue
        
        if not (len(group) == 2 and group[0].isdigit() and group[1].isalpha()):
            print("Invalid input. Please enter a valid group (e.g., 3A, 1B).")
            continue
        
        return group
    

def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Please enter the student's {subject} grade: "))
            if grade < 0 or grade > 100:
                print("Invalid input. Please enter a grade between 0 and 100.")
                continue
            return grade
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def validate_if_students_exist(students, name, group):
    for student in students:
        if student['name'] == name and student['group'] == group:
            return True
    return False


def validate_students_list(students):
    while True:
        if not students:
            try:
                print("\nNo students found")
                print("type 'back' to return to the main menu or 'add' to add a student.")
                option = input('Enter your option: ').lower()
                if option not in ('back','add'):
                    raise ValueError('\nInvalid input')
                if option == 'back':
                    return students
                elif option == 'add':
                    actions.add_student(students)
                    return students
            except ValueError as e:
                print(e)
                continue
        else:
            return students
        

def menu_empty_students_list():

    print("\nNo students found.")
    print('Type "back" to return to the main menu or "add" to add a student.')
    valid_options = ('back','add')
    while True:
        option = input('Enter your option: ').strip().lower()

        if option in valid_options:
            return option
        
        print('Invalid input. Please enter "back" to go back to the main menu or "add" to add a student.')



def menu_navigation_students_list():
    print('\nIf you want to go back to the main menu, please enter: "back". If you want to delete a student, please enter: "delete" or if you want to add a student, please enter: "add".')

    valid_options = ('back','delete','add')
    while True:
        option = input('Enter your option: ').strip().lower()

        if option in valid_options:
            return option
        
        print('Invalid input. Please enter "back" to go back to the main menu, "delete" to delete a student, or "add" to add a student.')
