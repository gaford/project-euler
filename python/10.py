# -*- coding: utf-8 -*-
# Project Euler 10

# an implementation of the Sieve of Erasthones
def sieve(n):
    """Return all primes <= n."""
    s = list(range(n+1)) # form a list of the integers <= n
    s[1] = 0 # get rid of 1
    sqrtn = int(round(n**0.5))
    # remove the multiples of natural numbers up to the square root of n
    for i in range(2, sqrtn + 1):
       	s[i**2: n+1: i] = [0] * len(range(i**2, n+1, i))
    return list(filter(None,s))

print(sum(sieve(2000000)))

# sum of the first 2000000 primes:  142913828922

