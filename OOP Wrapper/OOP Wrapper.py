def display_welcome():
    print('\n--- Python OOP project: Employee management system ---')
display_welcome()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f' {self.name} and {self.age}')




class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f'{self.salary} and {self.emp_id} ')





class Manager(Employee):
    def __init__(self, name, age, ID, salary, department):
        super().__init__(name, age, ID, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f'{self.department}')


people = []
employees = {}
managers = {}



def compare_salaries(emp1_id, emp2_id):
    emp1 = employees.get(emp1_id) or managers.get(emp1_id)
    emp2 = employees.get(emp2_id) or managers.get(emp2_id)

    if not emp1 or not emp2:
        print("Invalid employee IDs.")
        return

    print("\nComparing salaries:")
    if emp1.salary > emp2.salary:
        print(
            f"{emp1.__class__.__name__} {emp1.name} ({emp1.emp_id}) has a higher salary than {emp2.__class__.__name__} {emp2.name} ({emp2.emp_id}).")
    elif emp1.salary < emp2.salary:
        print(
            f"{emp1.__class__.__name__} {emp1.name} ({emp1.emp_id}) has a lower salary than {emp2.__class__.__name__} {emp2.emp_id}.")
    else:
        print(f"Both have the same salary.")





while True:
    print("\n--- Choose another operation ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input('Enter name:')
        age = input('Enter age:')
        person = Person(name, age)
        people.append(person)
        print(f'person created with name: {name} and age: {age}.')

    elif choice == '2':
        name = input('Enter name:')
        age = input('Enter age:')
        emp_id = input('Enter employee ID:')
        salary = input('Enter salary:')
        employee = Employee(name, age, emp_id, salary)
        employees[emp_id] = employee
        print(f'person created with name: {name}, age: {age}, ID: {id} and salary: {salary}.')

    elif choice == '3':
        name = input('Enter name:')
        age = input('Enter age:')
        emp_id = input('Enter employee ID:')
        salary = input('Enter salary:')
        department = input('Enter department:')
        manager = Manager(name, age, emp_id, salary, department)
        managers[emp_id] = manager
        print(f'person created with name: {name}, age: {age}, ID: {id}, salary: {salary} and {department}.')

    elif choice == '4':
        print('\nchoose details to show:')
        print('1. person')
        print('2. employee')
        print('3. manager')
        sub_choice = input('Enter your choice:')


        if sub_choice == '1':
            for person in people:
                print('\n person details:')
                person.show_details()

        elif sub_choice == '2':
            emp_id = input("Enter Employee ID: ")
            if emp_id in employees:
                print("\nEmployee details:")
                employees[emp_id].show_details()
            else:
                print("Employee not found.")

        elif sub_choice == '3':
            emp_id = input("Enter manager id: ")
            if emp_id in managers:
                print("\nManager Details:")
                managers[emp_id].show_details()
            else:
                print("Manager not found.")


    elif choice == '5':
        print("\nChoose two employees to compare salaries.")
        emp1_id = input("Enter the first employee's ID (e.g., E123): ")
        emp2_id = input("Enter the second employee's ID (e.g., M456): ")
        compare_salaries(emp1_id, emp2_id)

    elif choice == '6':
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")









