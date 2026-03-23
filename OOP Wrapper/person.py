def display_welcome():
    print('\n--- Python OOP project: Employee management system ---')
display_welcome()

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

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_detailes(self):
        print(f' {self.name} and {self.age}')

name = input('Enter name:')
age = input('Enter age:')
a = person(name, age)
print(f'person created with name: {name} nad age: {age}.')
a.show_detailes()



