# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:16:34 2016

@author: huiying
"""

# Ask the user for a string and print out whether this string is a palindrome 
# or not. 

user_input = input('Give me a string: ')
backwords = user_input[::-1]
if user_input == backwords:
    print('This string is a palindrome')
else:
    print('This string is not a palindrome')