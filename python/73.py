# Project Euler 73

from fractions import *

N = 8

fractions_list = []

for d in range(2, N + 1):
    n_min = d // 3 + 1
    n_max = d // 2 + 1
    fractions_list.extend([Fraction(n, d) for n in range(n_min, n_max)])

fractions_set = set(fractions_list)

print(len(fractions_set) - 1)






