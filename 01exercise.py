# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Ask user's name and age, and tell them the year they will 
# turn into 100 years old.
Name = input('Your name is: ')
Age = int(input('Your age is: '))
message = Name + ', you will turn into 100 years old at year '
message += str(2016 + 100 - Age)+'\n'
print(message)

# User decides how many copies of messages the program prints.
number = input('How many copies should I print: ')

print(int(number)*message)

