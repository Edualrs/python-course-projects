# BMI Calculator

name = input('Name: ')
weight = float(input('Weight: '))
height = float(input('Height: '))

bmi = weight / (height ** 2)

print()

print(f'Body Mass Index: {bmi:.2f}')

# Checking BMI table
if bmi <= 18.4:
    print('Underweight')
elif bmi <= 24.9:
    print('Normal')
elif bmi <= 39.9:
    print('Overweight')
else:
    print('Obese')