# Project Euler 69

from eulertools import Sieve, IsPrime1
from fractions import *

primes = Sieve(10**6)

def euler_totient(n):
    if IsPrime1(n):             # the answer if n is prime
        return n-1
    else:
        the_totient = n
        for p in primes:
            if p >= n**0.5 + 1:
                break
            elif n % p == 0:
                the_totient *= 1 - 1/p
    return the_totient

max_totient_ratio = 0
max_totient_ratio_index = 0
for n in range(1,10**6+1):
    if n / euler_totient(n) > max_totient_ratio:
        max_totient_ratio = n / euler_totient(n)
        max_totient_ratio_index = n

print(max_totient_ratio_index)


