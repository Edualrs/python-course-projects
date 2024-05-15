phrase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'.lower()


how_many_times = 0
number_of_times = 0
position = 0

while position < len(phrase):
    if phrase[position] == ' ':
        position += 1
        continue

    how_many_times = phrase.count(phrase[position])

    if how_many_times > number_of_times:
        letter_appars_more = phrase[position]
        number_of_times = how_many_times


    position += 1

print(f'{letter_appars_more} {number_of_times}')


