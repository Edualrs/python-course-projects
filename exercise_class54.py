# checking if a number is even

input_integer = input('Enter an integer: ')

try:
    integer = int(input_integer) # changing to integer only if the user entered an integer
    
    if (integer % 2) == 0: 
        print('Even')
    else:
        print('Odd')

except:
    print('This is not an integer')

# ========================================
...