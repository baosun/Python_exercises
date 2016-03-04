# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:25:58 2016

@author: huiying
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:16:28 2016

@author: huiying
"""

# Make a Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)
# one player is computer, another one is user.
# the rules: Rock beats scissors, Scissors beats paper, Paper beats rock

import random

user = input('What is your name? ')
computer = ['rock', 'paper', 'scissors']


# if user does not want to play
while True:
    print(user, ', do you want to play Rock-Paper-Scissors game?')
    player = input('y/n? ')
    if player != 'y':
        break

# if user wants to play
    print(user, ', rock, paper, scissors, which one do you choose?')
    play = input('You choose: ')
    comp = random.choice(computer)
    print('Computer choose: ', comp)
    
# handle tie
    if play == comp:
        print("It's a tie. You need to play a new game.\n")
    
        
# decide who wins       
    elif comp == 'rock':
        if play == 'paper':
            print(user, ', you win!\n')
        else:
            print(user, ', you lose!\n')
    elif comp == 'scissors':
        if play == 'rock':
            print(user, ', you win!\n')
        else:
            print(user, ', you lose!\n')
    elif comp == 'paper':
        if play == 'scissors':
            print(user, ', you win!\n')
        else:
            print(user, ', you lose!\n')
    

print('See you next time!\n')
    