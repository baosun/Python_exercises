# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:55:36 2016

@author: huiying
"""
# write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. 
# using at least one list comprehension.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)

print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] if i == j])

# Randomly generate two lists to test this
import random
print([i for i in random.sample(range(100), 11) for j in random.sample(range(100), 13) if i == j])