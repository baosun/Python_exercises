# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:09:11 2016

@author: huiying
"""
# Write one line that makes a new list that has only the even elements of list a.



print([i for i in [1, 4, 9, 16, 25, 36, 49, 64, 82, 100] if i % 2 == 0])

# print the eventh element
a = [1, 4, 9, 16, 26, 36, 49, 64, 82, 100]
print(a[1::2])

# print even element the for loop way
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)
