num = 10
print('Guess what I think?')
answer = input()

if answer < num:
    print('too small?')

if answer > num:
    print('too big?')

if answer == num:
    print('BINGO!')
