import numpy as np

def create_array():
    print('\nSelect the type of array to create:')
    print('1. 1D Array')
    print('2. 2D Array')
    print('3. 3D Array')
    choice=int(input('Enter your choice:'))

    if choice==1:
        n=int(input('Enter number of elements:'))
        elements=list(map(int,input(f'Enter {n} elements separated by space:').split()))
        arr=np.array(elements)

    elif choice==2:
        rows=int(input('Enter number of rows:'))
        cols=int(input('Enter number of columns:'))
        elements=list(map(int,input(f'Enter {rows*cols} elements separated by space:').split()))
        arr=np.array(elements).reshape(rows,cols)

    elif choice==3:
        x=int(input('Enter size in first dimension:'))
        y=int(input('Enter size in second dimension:'))
        z=int(input('Enter size in third dimension:'))
        elements=list(map(int,input(f'Enter {x*y*z} elements separated by space:').split()))
        arr=np.array(elements).reshape(x,y,z)

    else:
        print('Invalid choice!')
        return None
    print('Array created successfully:\n',arr)
    return arr


def mathematical_operations(arr):
    print('\nChoose a mathematical operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    choice=int(input('Enter your choice:'))

    elements=list(map(int,input(f'Enter the same-size array elements ({arr.size} elements separated by space):').split()))
    other=np.array(elements).reshape(arr.shape)

    print('\nOriginal Array:\n',arr)
    print('Second Array:\n',other)

    if choice==1:
        print('Result of Addition:\n',arr+other)
    if choice==2:
        print('Result of Subtraction:\n',arr-other)
    if choice==3:
        print('Result of Multiplication:\n',arr*other)
    if choice==4:
        print('Result of Division:\n',arr/other)
    else:
        print('Invalid choice!')


def combine_split_arrays(arr):
    print('\nChoose an option:')
    print('1. Combine Arrays')
    print('2. Split Array')
    choice = int(input('Enter your choice:'))

    elements=list(map(int,input(f'Enter the elements of another array ({arr.size} elements separated by space):').split()))
    other=np.array(elements).reshape(arr.shape)

    print('Original Array:\n',arr)
    print('Second Array:\n',other)

    if choice==1:
        combined=np.vstack((arr,other))
        print('Combined Array (Vertical Stack):\n',combined)
    elif choice==2:
        split_arrays=np.hsplit(arr,arr.shape[1])
        print('Split Arrays:')
        for part in split_arrays:
            print(part)
    else:
        print('Invalid choice!')


def search_sort_filter(arr):
    print('\nChoose an option:')
    print('1. Search a value')
    print('2. Sort the array')
    print('3. Filter values')
    choice = int(input('Enter your choice:'))

    if choice==1:
        val=int(input('Enter value to search:'))
        result=np.where(arr==val)
        print('Value found at:',result)
    elif choice==2:
        sorted_arr=np.sort(arr,axis=1)
        print('Sorted array:\n',sorted_arr)
    elif choice==3:
        threshold=int(input('Enter threshold value:'))
        filtered=arr[arr>threshold]
        print(f'Filtered values greater than {threshold}: {filtered}')
    else:
        print('Invalid choice!')


def aggregates_statistics(arr):
    print('\nChoose an aggregate/statistical operation:')
    print('1. Sum')
    print('2. Mean')
    print('3. Median')
    print('4. Standard Deviation')
    print('5. Variance')
    choice = int(input('Enter your choice:'))

    if choice==1:
        print('Sum of array:',np.sum(arr))
    elif choice==2:
        print('Mean of array:',np.mean(arr))
    elif choice==3:
        print('Median of array:',np.median(arr))
    elif choice==4:
        print('Standard deviation of array:',np.std(arr))
    elif choice==5:
        print('Variance of array:',np.var(arr))
    else:
        print('Invalid choice!')


def main():
    arr = None
    while True:
        print('\nWelcome to the NumPy Analyzer!')
        print("================================")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            arr = create_array()
        elif choice == 2 and arr is not None:
            mathematical_operations(arr)
        elif choice == 3 and arr is not None:
            combine_split_arrays(arr)
        elif choice == 4 and arr is not None:
            search_sort_filter(arr)
        elif choice == 5 and arr is not None:
            aggregates_statistics(arr)
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice or Array not created yet!")

if __name__ == "__main__":
    main()
