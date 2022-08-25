import random

min = 1
max = 99
counter=1
guess = random.randint(min, max)

print(guess)

answer = input()

while answer != 'd':
    # d== javab dorost hads zadeh shode ast

    if answer == 'k':
    # k == javab kochektar ast
        max = guess
        guess = random.randint(min, max)
        print(guess)

        answer = input()
    elif answer == 'b':
    # b== javab bozorgtar ast
        min = guess
        guess = random.randint(min, max)
        print(guess)
        answer = input()
    counter=counter+1
print('Wowwww!, I did it!')
print( counter, "tries to guess it right...")



