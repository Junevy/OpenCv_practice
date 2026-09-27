# print('hello')

score = 'A'

match score:
    case 'A':
        print('hello A')
    case 'B':
        print('hello B')
    case _:
        print('hello _')