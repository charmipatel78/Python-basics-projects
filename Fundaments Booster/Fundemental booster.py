print('welcome to the interactive personal data collector!')
name=(input('Enter your name:'))
age=int(input('Enter your age:'))
height=float(input('Enter your height cm:'))
fav_num=(input('Enter your favourite number:'))


print('\n here is the information :')
print(f' name: {name}')
print(f' age: {age}')
print(f' height: {height}')
print(f' fav_num: {fav_num}')


print('\ncovert into int to string')
age=20
n=str(age)
print(n)
print(type(n))

print('\nconvert into float to int')
height=5.5
n=int(height)
print(n)
print(type(n))

print('\n details of data types & memory address')
print(f' name: {name}  (Type: {type(name)}, memory address:{id(name)})')
print(f' age: {age}  (Type: {type(age)} ,memory address:{id(age)})')
print(f'height: {height}  (Type: {type(height)}, memory address:{id(height)})')
print(f' fav_num: {fav_num} (Type: {type(fav_num)}, memory address:{id(fav_num)})')

year=2025
age=20
birth_year=year-age
print('your birth year is approximately:',birth_year)

print('\n thank you for using the personal data collecter. goodbye!')






