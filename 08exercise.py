# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:16:28 2016

@author: huiying
"""

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# the rules: Rock beats scissors, Scissors beats paper, Paper beats rock


user1 = input('What is your name? ')
user2 = input('How about your name? ')


# if at least one user does not want to play
while True:
    print(user1, ', do you want to play Rock-Paper-Scissors game?')
    player1 = input('y/n? ')
    print(user2, ', how about you?')
    player2 = input('y/n? ')
    if player1 != 'y' or player2 != 'y':
        break

# if users want to play
    print(user1, ', rock, paper, scissors, which one do you choose?')
    play1 = input('You choose: ')
    print(user2, ' rock, paper, scissors, which one do you choose?')
    play2 = input('You choose: ')
    
# handle tie
    if play2 == play1:
        print("It's a tie. You need to play a new game.\n")
    
        
# decide who wins       
    elif play2 == 'rock':
        if play1 == 'paper':
            print(user1, ', you win!\n', user2, ', you lose!\n')
        else:
            print(user1, ', you lose!\n', user2, ', you win!\n')
    elif play2 == 'scissors':
        if play1 == 'rock':
            print(user1, ', you win!\n', user2, ', you lose!\n')
        else:
            print(user1, ', you lose!\n', user2, ', you win!\n')
    elif play2 == 'paper':
        if play1 == 'scissors':
            print(user1, ', you win!\n', user2, ', you lose!\n')
        else:
            print(user1, ', you lose!\n', user2, ', you win!\n')
    i = i+1

print('Cannot play. We need 2 players.')
print('See you next time!\n')
    