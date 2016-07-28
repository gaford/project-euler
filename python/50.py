# -*- coding: utf-8 -*-
# Project Euler 50

from eulertools import Sieve, IsPrime1

# prime is larger than 958577, the sum of the first 536 primes

Primes = Sieve(10**6)

N = 10**3

PrimeSums = []

for M in range(N):
    PrimeSums.append(sum(Primes[:M]))

sum_lengths = [[] for j in range(600)]

for k in range(N):
    for j in range(len(PrimeSums)):
        candidate = PrimeSums[j] - PrimeSums[k]
        if candidate > 958577 and candidate < 1000000:
            if IsPrime1(candidate):
                sum_lengths[j-k].append(candidate)
                # if j - k == 543:
                #     print(j,k)

print(sum_lengths) # 997651, a sum of 543 primes (546 length - 3 length)

# for j in range(len(sum_lengths)):
#     if sum_lengths[j] != []:
#         print(j) # 543 is the longest chain length