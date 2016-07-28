# -*- coding: utf-8 -*-
# Project Euler 6

# difference between sum of first 100 natural numbers squared and squares of
# first 100 natural numbers

# smarter way:  use the formulae for the sums of integers and the sums of
# square integers

a = sum(range(101))

hundredSquares = [x**2 for x in range(101)]

b = sum(hundredSquares)

print(a**2 - b)
