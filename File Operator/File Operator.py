print('Welcome to personal journal manager!')
print('Please select an option:')

import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename='journal.txt'):
        self.filename = filename

    def add_entry(self):
        a = input('Enter your journal entry:\n')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            with open (self.filename,'a') as file:
                file.write(f'{timestamp} - {a}\n')
            print('Entry added successfully.')
        except Exception as e:
            print(f'ERROR: {e}')

    def view_entries(self):
        try:
            with open(self.filename,'r') as file:
                content = file.read()
                if content.strip() == '':
                    print('journal is empty.')
                else:
                    print('journal entries:\n' + content)
        except FileNotFoundError:
            print('file is missing!!')
        except Exception as e:
            print(f'ERROR: {e}')


    def search_entries(self):
        keyword = input('Enter your keyword to search:')
        try:
            with open(self.filename,'r') as file:
                c = file.read()
                entry = c.strip().split('\n\n')
                found = 0
                print(entry)
                for i in entry:
                    if keyword.lower() in i.lower():
                       print(i)
                       found = 1

                if found == 0:
                    print('No entries found.')

        except FileNotFoundError:
            print('file iss missing!')
        except Exception as e:
            print(f'ERROR: {e}')

    def delete_entries(self):
        confirm = input('Are you sure you want to delete all entries:')
        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print('journal entries deleted.')
            except FileNotFoundError:
                print('file is missing!')
            except Exception as e:
                print(f'ERROR: {e}')
        else:
            print('file is closed')

j = JournalManager()
while True:
    try:
        print('\n Journal Menu')
        print('1. Add a new entry')
        print('2. View all entries')
        print('3. Search for an entry')
        print('4. Delete all entries')
        print('5. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            j.add_entry()
        elif choice == '2':
            j.view_entries()
        elif choice == '3':
            j.search_entries()
        elif choice == '4':
            j.delete_entries()
        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice.')
    except ValueError as e:
        print(f'ERROR: {e}')




