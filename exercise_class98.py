import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))

# First digit

sum_of_digits = 0
digit_index = 0

for countdown in range(10,1,-1):
    # sum of digits multiplied by countdown from ten
    mult_by_countdown_from_ten = int(cpf[digit_index]) * countdown
    sum_of_digits += mult_by_countdown_from_ten

    digit_index += 1

first_digit = (sum_of_digits * 10) % 11
first_digit = first_digit if first_digit < 10 else 0

# Second digit

first_ten_digits = cpf + str(first_digit)

sum_of_digits = 0
digit_index = 0

for countdown in range(11,1,-1):
    # sum of digits multiplied by countdown from ten
    mult_by_countdown_from_eleven = int(first_ten_digits[digit_index]) * countdown
    sum_of_digits += mult_by_countdown_from_eleven

    digit_index += 1

second_digit = (sum_of_digits * 10) % 11
second_digit = second_digit if second_digit < 10 else 0

# validating

validation_digits = str(first_digit) + str(second_digit)
# validating = 'Valid' if validation_digits == cpf[-2:] else 'Invalid'

full_cpf = cpf + validation_digits

print(full_cpf)