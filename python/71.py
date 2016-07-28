# Project Euler 71

from fractions import *

N = 10**6

fraction_list = []

for d in range(2,N + 1):
    n = 3 * d // 7
    fraction_list.append(Fraction(n, d))

fraction_list.sort()

x = fraction_list.index(Fraction(3, 7))

print(x) # 857142
print(fraction_list[x-1]) # 428570/999997

