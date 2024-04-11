# Bigger than that

first_value = input('Enter a value: ')
second_value = input('Enter another value: ')

statement = '\nValue "{0}" is greater than or equal to the value "{1}"'

if first_value >= second_value:
    print(statement.format(first_value, second_value))
else:
    print(statement.format(second_value, first_value))