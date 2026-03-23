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

from person import person
from employee import Employee
from manager import manager

x = [person('jhon doe',30)]
y = [Employee('jane smith', 28, 123,  50000)]
z = [manager('alice johnson', 40, 456,  80000, 'sales')]
def main():
    print('\nchoose detailes to show:')
    print('1. person')
    print('2. employee')
    print('3. manager')
main()

choice = input('Enter your choice:')
print('employee Detailes:')
if choice == '1':
    for a in x:
        a.show_detailes()

elif choice == '2':
    for b in y:
        b.show_detailes()

elif choice == '3':
    for c in z:
        c.show_detailes()


