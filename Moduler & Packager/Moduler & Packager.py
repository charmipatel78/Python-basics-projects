import datetime
import time
import math
import random
import string
import uuid
import os

def datetime_operations():
    while True:
        print('\nDatetime and Time Operations:')
        print('1. Display current date and time')
        print('2. Calculate difference between two dates/times')
        print('3. Format date into custom format')
        print('4. Stopwatch')
        print('5. Countdown Timer')
        print('6. Back to Main Menu')
        choice = int(input("Enter your choice: "))

        if choice==1:
            now = datetime.datetime.now()
            print('\nCurrent Date and Time:', now.strftime('%Y-%m-%d %H:%M:%S'))

        elif choice==2:
            d1=input('Enter the first date (YYYY-MM-DD):')
            d2=input('Enter the second date (YYYY-MM-DD):')
            date1=datetime.datetime.strptime(d1,'%Y-%m-%d')
            date2=datetime.datetime.strptime(d2,'%Y-%m-%d')
            diff=abs((date2-date1).days)
            print(f"Difference: {diff} days")

        elif choice==3:
            str=input('Enter date (YYYY-MM-DD):')
            obj=datetime.datetime.strptime(str,'%Y-%m-%d')
            x=input('Enter format (e.g.%d/%m/%Y):')
            print('Formatted Date:',obj.strftime(x))

        elif choice==4:
            input('Press Enter to start stopwatch')
            start = time.time()
            input('Press Enter to stop stopwatch')
            end = time.time()
            print(f'Elapsed Time: {end - start:.2f} seconds')

        elif choice==5:
            sec=int(input('Enter countdown time in seconds:'))
            for i in range(sec,0,-1):
                print(i,end=' ',flush=True)
                time.sleep(1)
            print('\nTime’s up!')

        elif choice==6:
            break

        else:
            print('Invalid choice!')

def math_operations():
    while True:
        print('\nMathematical Operations:')
        print('1. Calculate Factorial')
        print('2. Solve Compound Interest')
        print('3. Trigonometric Calculations')
        print('4. Area of Geometric Shapes')
        print('5. Back to Main Menu')
        choice = int(input('Enter your choice:'))

        if choice==1:
            num=int(input('Enter a number:'))
            print('Factorial:',math.factorial(num))

        elif choice==2:
            a=float(input("Enter principal amount: "))
            b=float(input("Enter rate of interest (in %): ")) / 100
            c=float(input("Enter time (in years): "))
            d=a*((1+b)**c)
            print(f'Compound Interest:{d:.2f}')

        elif choice==3:
            angle=math.radians(float(input('Enter angle in degrees:')))
            print(f'sin:{math.sin(angle):.2f},cos: {math.cos(angle):.2f},tan: {math.tan(angle):.2f}')

        elif choice==4:
            print('1. Area of Circle')
            print('2. Area of Rectangle')
            print('3. Area of Triangle')
            sub = int(input('Enter your choice:'))
            if sub==1:
                r=float(input('Enter radius:'))
                print('Area of Circle:',math.pi*r*r)
            elif sub==2:
                l=float(input('Enter length:'))
                b=float(input('Enter breadth:'))
                print('Area of Rectangle:',l*b)
            elif sub==3:
                b=float(input('Enter base:'))
                h=float(input('Enter height:'))
                print('Area of Triangle:',0.5*b*h)

        elif choice==5:
            break

        else:
            print('Invalid choice!')

def random_data():
    while True:
        print('\nRandom data generation:')
        print('1. Generate random number')
        print('2. Generate random list')
        print('3. Create random password')
        print('4. Generate random OTP')
        print('5. Back to Main Menu')
        choice=int(input('Enter your choice:'))

        if choice==1:
            print('Random Number:',random.randint(1,100))

        elif choice==2:
            a1=[random.randint(1,50) for _ in range(5)]
            print('Random list:',a1)

        elif choice==3:
            length=int(input('Enter password length:'))
            char=string.ascii_letters+string.digits+string.punctuation
            password=''.join(random.choice(char) for _ in range(length))
            print('Generated Password:',password)

        elif choice==4:
            otp=''.join(random.choice(string.digits) for _ in range(6))
            print('Generate OTP:',otp)

        elif choice==5:
            break

        else:
            print('Invalid choice!')

def generate_uuid():
    print('\nGenerated UUID:',uuid.uuid4())


def file_operations():
    while True:
        print('\nFile operations:')
        print('1. Create a new file')
        print('2. Write to a file')
        print('3. Read from a file')
        print('4. Append to a file')
        print('5. Back to Main Menu')
        choice=int(input('Enter your choice'))

        if choice==1:
            filename=input('Enter file name:')
            open(filename,'w').close()
            print('File created successfully!')

        elif choice==2:
            filename=input('Enter file name:')
            data=input('Enter data to write:')
            with open(filename,'w') as f:
                f.write(data)
            print('Data written successfully!')

        elif choice==3:
            filename=input('Enter file name:')
            with open(filename,'r') as f:
                print('File content:\n',f.read())

        elif choice==4:
            filename=input('Enter file name:')
            data=input('Enter data to append:')
            with open(filename, 'a') as f:
                f.write(data)
            print('Data append successfully!')

        elif choice==5:
            break

        else:
            print('Invalid choice!')

def explore_module():
    module_name=input('Enter module name to explore:')
    mod=__import__(module_name)
    print('Available Attributes in',module_name,'module:\n',dir(mod))


while True:
    print('\n---------------------')
    print('Welcome to multi-utility Toolkit')
    print('------------------------')
    print('1. Datetime and Time operations')
    print('2. Mathematical operations')
    print('3. Random data generation')
    print('4. Generate unique identifiers (UUID)')
    print('5. File operations (custom module)')
    print('6. Explore module attributes (dir())')
    print('7. Exit')
    print('---------------------------')
    choice=int(input('Enter your choice:'))

    if choice==1:
        datetime_operations()
    elif choice==2:
        math_operations()
    elif choice==3:
        random_data()
    elif choice==4:
        generate_uuid()
    elif choice==5:
        file_operations()
    elif choice==6:
        explore_module()
    elif choice==7:
        print('Thank you for using multi-utility Toolkit!')
        break
    else:
        print('Invalid choice!')






