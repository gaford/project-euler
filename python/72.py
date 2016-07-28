# Project Euler 72

from eulertools import Sieve, IsPrime1

N = 10**4

primes = Sieve(10**6)

def euler_totient(n):
    """Returns the Euler totient function of n."""
    if IsPrime1(n):             # the answer if n is prime
        return n-1
    else:
        the_totient = n
        for p in primes:
            if p >= n // 2 + 1:
                break
            elif n % p == 0:
                the_totient *= 1 - 1/p
    return the_totient

the_sum = 0
for n in range(2, N + 1):
    the_sum += euler_totient(n)

print(the_sum) #


