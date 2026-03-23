def display_welcome():
    print('Welcome to the pattern generator and number analyzer!\n')
display_welcome()

def display_menu():
    print('Select an option:')
    print('1. Generate a pattern')
    print('2. Analyze a range of numbers')
    print('3. Exit')
display_menu()
print(input('Enter your choice number:'))

def pattern_generator():
    try:
        rows = int(input('Enter the number of rows for the pattern:'))

        if rows <= 0:
            print('row count must be a positive number.')
            return
        print('\npattern:')
        for i in range (1, rows + 1):
            print('*' * i)
    except ValueError:
        print('Invalid input. please enter a valid number.')
pattern_generator()

def number_analysis():
    try:
        start = int(input('Enter the start of the range:'))
        end = int(input('Enter the end of the range:'))
        if start > end:
            print('Start must be less than or equal to end.')
            return
        total = 0
        print()
        for num in range (start, end + 1):
            if num % 2 == 0:
                print(f'Number {num} is Even')
            else:
                print(f'Number {num} is Odd')
            total += num
        print(f'\nsum of all numbers from {start} to {end} is: {total}')
    except ValueError:
        print('Invalid input. please enter numbers only.')


def main():
    display_welcome()
    while True:
        display_menu()
        choice = input('Enter your choice:')
        if choice == '1':
            pattern_generator()
        elif choice == '2':
            number_analysis()
        elif choice == '3':
            print('Existing the programme. Goodbye!')
            break
        else:
            print('Invalid choice. please enter 1, 2 or 3.')
main()
