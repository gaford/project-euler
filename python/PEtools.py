# -*- coding: utf-8 -*-
# Tools for Project Euler Problems

# an implementation of the Sieve of Erasthones
def Sieve(n):
    # Return all primes <= n.
    s = list(range(n+1)) # form a list of the integers <= n
    s[1] = 0 # get rid of 1
    sqrtn = int(round(n**0.5))
    # remove the multiples of natural numbers up to the square root of n
    for i in range(2, sqrtn + 1):
        s[i**2: n+1: i] = [0] * len(range(i**2, n+1, i))
    return list(filter(None,s))

# a simple primality test
def IsPrime1(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# sum of proper divisors
def ProperDivisorSum(n):
	# Returns the sum of the proper divisors of n.
    divisors = {1}
    for j in range(2,int(n**0.5 + 1)):
        if n % j == 0:
            divisors = divisors.union({j}).union({n//j})
    return sum(divisors)

def Choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
