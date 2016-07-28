# -*- coding: utf-8 -*-
# Project Euler 47

from eulertools import Sieve

N = 10**6

Primes = Sieve(N)

def FourDivisorTest(x):
	primeDivisors = []
	limit = int(x**0.5) + 2
	for p in Primes[:limit]:
		if x % p == 0:
			primeDivisors.append(p)
	if len(primeDivisors) == 4:
		return True
	else:
		return False

for n in range(1,N):
    if not FourDivisorTest(n):
        pass
    else:
        if not FourDivisorTest(n+1):
            pass
        else:
            if not FourDivisorTest(n+2):
                pass
            else:
                if not FourDivisorTest(n+3):
                    pass
                else:
                    print(n)
                    break
