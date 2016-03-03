# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:39:29 2016

@author: huiying
"""

# ask for 2 numbers, and tell whether the second number can divides evenly
# into the first number.
num = int(input('Give me a number: '))
check = int(input('Give me another number: '))
if num % check == 0:
    print(str(check) + ' divides evenly into ' + str(num))
else:
    print(str(check) + ' does not divide evenly into ' + str(num))



# ask for a number, and tell whether the number can be divited by 4, or 
# odd or even.
number = int(input('Give me a number: '))
if number % 4 == 0:
    print('This is a multiple of 4')
elif number % 2 == 0:
    print('This is an even number')
else:
    print('This is an old number')