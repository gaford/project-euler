# -*- coding: utf-8 -*-
# Project Euler 1

multiples = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]

multipleSum = sum(multiples)

print(multipleSum)

