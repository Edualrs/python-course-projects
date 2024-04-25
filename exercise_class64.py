# Iterating strings with while

name = input('Name: ')

name_with_asterisk = ''
iteration = 0

while iteration < len(name):
    name_with_asterisk += f'*{name[iteration]}'
    iteration += 1

print(name_with_asterisk)