# Project Euler 64

from math import sqrt, floor
# from fractions import *
# from decimal import *

def next_term(a,b,c):
    return floor((a + b) / c)

def cont_frac_sqrt(n):
    """Returns the continued fraction expansion of sqrt(n)."""
    if sqrt(n).is_integer():
        return '[%s]' % int(sqrt(n))

    m = [0]
    d = [1]
    a = [int(sqrt(n))]

    while True:
        m.append(d[-1] * a[-1] - m[-1])
        d.append(round((n - m[-1]**2) / d[-1]))
        a.append(next_term(a[0], m[-1], d[-1]))

        if a[-1] == 2 * a[0]:
            break

    return_string = '[' + str(a[0]) + ';'
    for j in range(1,len(a)):
        return_string += ' ' + str(a[j]) + ','

    return_string = return_string[:-1] + ']'

    return return_string

def cont_frac_sqrt_period(n):
    """Returns the continued fraction expansion of sqrt(n)."""
    if sqrt(n).is_integer():
        return 0

    m = [0]
    d = [1]
    a = [int(sqrt(n))]

    while True:
        m.append(d[-1] * a[-1] - m[-1])
        d.append(round((n - m[-1]**2) / d[-1]))
        a.append(next_term(a[0], m[-1], d[-1]))

        if a[-1] == 2 * a[0]:
            break

    return len(a) - 1

N = 10000

count = 0
for n in range(N + 1):
    if cont_frac_sqrt_period(n) % 2 == 1:
        count += 1

print(count) # 1322

