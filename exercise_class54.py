# Checking if a number is even

# input_integer = input('Enter an integer: ')

# try:
#     integer = int(input_integer) # changing to integer only if the user entered an integer
    
#     if (integer % 2) == 0: 
#         print('Even')
#     else:
#         print('Odd')

# except ValueError:
#     print('This is not an integer')

# ========================================
# Appropriate greeting

from time import strftime

current_time = strftime('%H') # getting the current time

try:
    current_time_int = int(current_time)

    # checking if the time format is in the standart 24 hour time length
    if current_time_int >= 0 and current_time_int <= 23:

        if current_time_int <= 11:
            print('Good Morning!')
        elif current_time_int <= 17:
            print('Good Afternoon!')
        else:
            print('Good Evening!')

    else:
        print('Invalid format')

except ValueError: # if the input is not already a number
    print('Invalid value')

# ========================================
# Name size

# first_name = input('First name: ')
# name_size = len(first_name)

# # checking that the user did not enter an invalid name lenght or format
# if name_size > 1 and not first_name.isdigit():

#     if name_size <= 4:
#         print(f'{name_size} letters. Your name is too short!')
#     elif name_size <= 6:
#         print(f'{name_size} letters. Um ok, your name is normal')
#     else:
#         print(f'{name_size} letters. Wow, your name is really big!')

# else:
#     print(f"{first_name} right? ... but what's your name?")