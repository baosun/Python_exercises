# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 23:30:55 2016

@author: huiying
"""
# generate 2 random lists, and find the commen elements of the lists
import random
a = []
for i in range(0, 20): 
    i = random.randint(0,100)
    a.append(i)
b = []
for j in range(0, 20):
    j = random.randint(0, 100)
    b.append(j)
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)