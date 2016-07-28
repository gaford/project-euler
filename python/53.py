# Project Euler 53

from eulertools import Choose

N = 0

for n in range(23,101):
    for r in range(0,n):
        if Choose(n, r) > 10**6:
            N += 1

print(N) # 4075

