def display_welcome():
    print('welcome to the student data organizer!')
    print('This program helps store, manage, and display student records.\n')
display_welcome()

students = {}

def add_students():
    name = input('Enter student name:')
    age = int(input('Enter age:'))
    grade = input('Enter grade:')
    subjects = set(input('Enter subjects (comma-separated):').split(','))
    student_id = input('Enter student ID:')
    dob = input('Enter date of birth (DD-MM-YYYY):')

    students[student_id] = {
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects,
        'details': (student_id, dob)
    }
    print('student added successfully.\n')

def display_all_students():
    if not students:
        print('No student records found.\n')
        return
    for sid, info in students.items():
        print(f'ID: {sid}')
        print(f'name: {info['name']}, age: {info['age']}, grade: {info['grade']}')
        print(f'subjects: {','.join(info['subjects'])}')
        print(f'date of birth: {info['details'][1]}')
        print('_' * 40)

def update_student():
    sid = input('Enter student ID to update:')
    if sid in students:
        print('1. update age\n2. update subjects')
        choice = input('choose option (1 or 2):')
        if choice == '1':
            new_age = int(input('Enter new age:'))
            students[sid]['age'] = new_age
            print('age updated successfully.\n')
        elif choice == '2':
            new_subjects = set(input('Enter new subjects (comma-separated):').split(','))
            students[sid]['subjects'] = new_subjects
            print('subjects updated successfully.\n')
        else:
            print('Invalid choice.\n')
    else:
        print('student ID not found.\n')

def delete_student():
    sid = input('Enter student ID to delete:')
    if sid in students:
        del students[sid]
        print('student record deleted successfully.\n')
    else:
        print('student ID not found.\n')

def display_subjects():
    all_subjects = set()
    for info in students.values():
        all_subjects.update(info['subjects'])
    print('subjects offered:',','.join(sorted(all_subjects)) + '\n')

def exit_program():
    print('Thank you for using the student data organizer. Goodbye!\n')

def main():
    while True:
        print('\nmenu:')
        print('1. add student')
        print('2. display all students')
        print('3. update student information')
        print('4. delete student')
        print('5. display subjects offered')
        print('6. exit')

        choice = input('Enter your choice (1-6):')

        if choice == '1':
            add_students()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects()
        elif choice == '6':
            exit_program()
            break
        else:
            print('Invalid choice. try again.\n')

main()

