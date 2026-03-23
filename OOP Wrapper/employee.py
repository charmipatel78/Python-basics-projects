from person import person
class Employee(person):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age)
        self.ID = ID
        self.salary = salary

    def Show_Detailes(self):
        super().show_detailes()
        print(f'{self.salary} and {self.ID} ')

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
b = Employee(name, age, ID, salary)
print(f'person created with name: {name}, age: {age}, ID: {ID} and salary: {salary}.')
b.show_detailes()

