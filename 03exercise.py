# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 23:03:04 2016

@author: huiying
"""

# ask for a number, and find the elements of list a that is less than
# the give numer.
num = int(input('Give me a number: '))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < num:
        b.append(i)
print(b)
        
# one line to find the elements of a that is less than 5
print([ i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5])