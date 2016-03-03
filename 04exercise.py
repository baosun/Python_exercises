# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 23:20:30 2016

@author: huiying
"""
# ask for a number and find all the divisors of the number
num = int(input('Give me a number '))
divisors = []
for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)
print(divisors)