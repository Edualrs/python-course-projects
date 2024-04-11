# Form

from datetime import date

first_name = input('First name: ')
last_name = input('Last name: ')
year_of_birth = int(input('Year of birth: '))
height = float(input('Height (meters): '))

current_year = date.today().year
age = current_year - year_of_birth

print() # break

print(f'Name: {first_name} {last_name}')
print(f'Age: {age}')
print(f'Year of birth: {year_of_birth}')
print(f'Legal age: {age >= 18}')
print(f'Height: {height} m')

