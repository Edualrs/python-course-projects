import os

secret_word = 'capivara'
letters_found = ''
attempts_made = 0

while True:
    hidden_secret_word = ''
    
    attempt = input('Enter a letter: ')
    os.system('cls')

    if len(attempt) != 1:
        print('Type just one letter')
        print()

        continue

    if attempt not in letters_found:
        if attempt in secret_word:
            letters_found += attempt

    
        for letter in secret_word:
            if letter not in letters_found:
                hidden_secret_word += '*'
            else:
                hidden_secret_word += letter

        print(hidden_secret_word)
        print(attempts_made, 'attempts made')

        print()

        attempts_made += 1

        if '*' not in hidden_secret_word:
            print('Congratulations, you got it right!')
            print(attempts_made, 'attempts made')

            break

    else:
        print('This letter has already been found, try another')
        print()

        continue
    
        
