import os

shopping_list = ['Macarrão', 'Cebola']

while True:
    for index, item in enumerate(shopping_list):
        print(index, item)
    
    print()
    print('[A]dd [D]elete [E]xit')

    user_input = input()[0].lower()
    
    if user_input == 'a':
        print()
        
        new_item = input('New item: ')
        shopping_list.append(new_item)
        ...

        os.system('cls')

    elif user_input == 'd':
        print()
        try:
            delete_item = int(input('Delete item in index: '))
            del shopping_list[delete_item]

        except IndexError:
            os.system('cls')
            
            print('Item not found')
            print()

        except ValueError:
            os.system('cls')

            print('Just enter the item index')
            print()
        ...

    elif user_input == 'e':
        print('Leaving...')
        break
        ...

    else:
        os.system('cls')

        print('Unknown command')
        print()