# Simple Calculator
while True:
    number1_preformatted = input('First number: ')
    number2_preformatted = input('Second number: ')

    operator = input('Calculation operator: ')

    try:
        number1 = int(number1_preformatted)
        number2 = int(number2_preformatted)

    except ValueError:
       print()
       print('Type numbers only')
       print()

       continue

    if operator == '+':
        print()
        print(f'{number1} {operator} {number2} = {number1 + number2}')
    elif operator == '-':
       print()
       print(f'{number1} {operator} {number2} = {number1 - number2}')
    elif operator == '*':
        print()
        print(f'{number1} {operator} {number2} = {number1 * number2}')
    elif operator == '/':
        print()
        print(f'{number1} {operator} {number2} = {number1 / number2}')
    else:
        print()
        print('Invalid operator')

    print()

    turn_off = input('Do you want to turn off the calculator? [Y]es [N]o \n')
    print()
    
    try:
        if turn_off[0].upper() == 'Y':
            break
    except IndexError:
        continue

