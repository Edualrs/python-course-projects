# Differents name formatting

name = input('Type your name: ')
age = input('Enter your age: ')

print()

if name and age:
    print(f'Your name is {name}')
    print(f'Your reversed name is {name[::-1]}')

    if ' ' in name:
        print(f'Your name contains spaces')
    else:
        print('Your name does not contain spaces')

    # Below I break the name into parts, and add the numbers of characters in 
    # each part of the name, without the spaces
    print('Your name has ' \
        f'{sum(len(parts_name) for parts_name in name.split())} letters')
    
    print(f'First letter of your name is "{name[0].upper()}"')
    print(f'Last letter of your name is "{name[-1].upper()}"')

else:
    print('Sorry, you left fields empty 😢')
    

