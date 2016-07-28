# Project Euler 70

from eulertools import Sieve, IsPrime1

primes = Sieve(10**4)

def euler_totient(n):
    """Returns the Euler totient function of n."""
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

def is_permutation(x,y):
    """Checks if x and y are digital permutations of one another."""
    x_string = sorted(str(x))
    y_string = sorted(str(y))
    return (x_string == y_string)

the_sum = 0

for n in range(2,10**6):
    the_sum += euler_totient(n)

print(the_sum)


