# -*- coding: utf-8 -*-
# Project Euler 46

from eulertools import Sieve
from math import sqrt

N = 10**4

Primes = set(Sieve(N))
Evens = {2*n for n in range(N//2)}

Goldbach = set()

for p in Primes:
	for n in range(int(N**0.5)):
		Goldbach = Goldbach | {p + 2 * n**2}

Leftovers = sorted(set(range(N)) - Primes - Evens - Goldbach - {1})

print(Leftovers[0]) # 5777





