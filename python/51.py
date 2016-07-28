# -*- coding: utf-8 -*-
# Project Euler 51

# want an 8 prime family

from eulertools import Sieve, IsPrime1

primes = Sieve(10**6)

big_primes = primes[primes.index(56003) + 1:]

def eight_prime_chain_test(p):
    """Tests for whether digit replacement in p produces a chain of eight
    primes."""
    digits = {x for x in str(p)}
    for digit_string in digits:
        prime_chain = set()
        for n in range(10):
            test = int(str(p).replace(digit_string,str(n)))
            if IsPrime1(test) and not str(test).startswith('0'):
                prime_chain = prime_chain | {test}
        if len(prime_chain) >= 8:
            print(sorted(prime_chain))
            return True
        else:
            return False

for p in big_primes:
    if eight_prime_chain_test(p):
        break

# 121313

