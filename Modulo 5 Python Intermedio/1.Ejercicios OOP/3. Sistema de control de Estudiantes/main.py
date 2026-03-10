from students import data
from students import actions



def load_main_menu():
    while True: 
        print('\nWelcome to the Student Control System')
        print("\n=== MAIN MENU ===")
        print('1. Add a student')
        print('2. View all students')
        print('3. View the top 3 students with the highest average grade')
        print('4. View all the failed students (average grade below 60)')
        print("5. View Students' overall average")
        print('6. Export the students data to a CSV file')
        print('7. Import students data from a CSV file')
        print('8. Exit')
        try:
            option = int(input('Please enter an option number: '))
            if option < 1 or option > 8:
                print("Invalid option. Please enter a number between 1 and 8.")
                continue
            elif option == 8:
                print("Exiting the program. Goodbye!")
                exit()
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
        
        return option

    

def main():
    students = []
    while True:
        option = load_main_menu()

        if option == 1:#Add a student
            actions.Student.add_student(students)
            # actions.add_student(students)
        elif option == 2:#View all students
            actions.get_all_students(students)
        elif option == 3:#View the top 3 students with the highest average grade
            actions.get_top_students(students)
        elif option == 4:#View all the failed students (average grade below 60)
            actions.get_failed_students(students)
        elif option == 5:#View Students' overall average
            actions.students_avg(students)
        elif option == 6:#Export the students data to a CSV file
            data.export_students_to_csv(students)
        elif option == 7:#Import students data from a CSV file
            data.import_students_csv(students)




if __name__ == '__main__':
    main()