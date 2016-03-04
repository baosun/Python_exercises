# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:37:56 2016

@author: huiying
"""

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, 
# then tell them whether they guessed too low, to high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken
# when the game ends, print this out.

import random

i = 0
while True:
    rand = random.randint(1, 9)
    print('Do you want to play?')
    play = input('yes/exit: ')

    if play == 'exit':
        break
    else:
        user = int(input('Guess the number in my mind: '))
        print('The number in my mind is ', rand)
        if rand == user:
            print('You guessed exactly right!\n')
        elif rand <= user:
            print('You guessed too high\n')
        else:
            print('You guessed too low\n')
        i += 1
        
print('You guessed', i, 'times! Good job!')
print('See you next time!\n')