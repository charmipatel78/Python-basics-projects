from employee import  employee
class manager(employee):
    def __init__(self, name, age, ID, salary, department):
        super().__init__(name, age, ID, salary)
        self.department = department

    def show_detailes(self):
        super().show_detailes()
        print(f'{self.department}')

print('\n--- Choose another option ---')

def display_menu():
    print('Choose an operation:')
    print('1. create a person')
    print('2. Create an employee')
    print('3. Create a manager')
    print('4. Show details')
    print('5. Compare salaries')
    print('6. Exit')
    print(input('\nEnter your choice:'))
display_menu()

name = input('Enter name:')
age = input('Enter age:')
ID = input('Enter employee ID:')
salary = input('Enter salary:')
department = input('Enter department:')
c = manager(name, age, ID, salary, department)
print(f'person created with name: {name}, age: {age}, ID: {ID}, salary: {salary} and {department}.')
c.show_detailes()




