def display_welcome():
    print('Welcome  to the data analyzer and transformer program!\n')
display_welcome()

def display_menu():
    print('1. Input Data')
    print('2. Display Data summary (Built-in functions)')
    print('3. Calculate Factorial (Recursion)')
    print('4. Filter data by threshold (Lambda function)')
    print('5. Sort Data')
    print('6. Display datasets statistics (Return multiple values)')
display_menu()
print(input('Please enter your choice:'))

def input_data():
    data = input('Enter data for a 1D array (separated by spaces):')
    return list(map(int, data.split()))
data = input_data()
print('data has been stored successfully!\n')

print(input('please enter your choice:'))
def display_summary(data):
    print('\ndata summary:')
    print(f'total elements: {len(data)}')
    print(f'minimum value: {min(data)}')
    print(f'maximum value: {max(data)}')
    print(f'sum of all values: {sum(data)}')
    print(f'average value: {sum(data)/len(data)}')
display_summary(data)
print(input('please enter your choice:'))
num = int(input('Enter a number to calculate its factorial:'))
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(f'factorial of {num} is: {factorial(num)}')

print(input('please enter your choice:'))
threshold = int(input('Enter a threshold value to filter out data about this value:'))
def filter_data(data, threshold):
    filtered = list(filter(lambda x: x >= threshold, data))
    return filtered

filtered_result = filter_data(data, threshold)
print(f'filtered data (values >= {threshold}):')
print(', '.join(map(str, filtered_result)))
filter_data(data, threshold)

print(input('please enter your choice:'))
print('choose sorting option:')
print('1. ascending')
print('2. descending')
sort_choice = input('enter your choice:')
def sort_data(data):
    if sort_choice == '1':
        sorted_data = sorted(data)
        order = 'ascending'
    elif sort_choice == '2':
        sorted_data = sorted(data, reverse=True)
        order = 'descending'
    else:
        print('invalid choice.')
        return
    print(f'sorted data in {order} order:')
    print(', '.join(map(str, sorted_data)))
sort_data(data)

print(input('please enter your choice:'))
def get_statistics(data):
    print('dataset statistics:')
    print(f' minimum value: {min(data)}')
    print(f' maximum value: {max(data)}')
    print(f' sum of all values: {sum(data)}')
    print(f' average value: {sum(data)/len(data)}')
get_statistics(data)

print(input('please enter your choice:'))
def Exit():
    print('\nThank you for using the data analyzer and transformer program. Goodbye!')
Exit()











