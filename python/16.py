# -*- coding: utf-8 -*-
# Project Euler 16

x = str(2**1000) # the number as a string

y = list(x) # the list of its digits as strings

z = [int(a) for a in y] # the list of its digits as integers

print(sum(z)) # their sum, 1366





