# Project Euler 64

from math import sqrt, floor

# Pell's equation

""" Continued fraction functions. """

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

    return a

def find_minimal_Pell_solution(D):
    """Find the minimal solution to Pell's equation with D the non-square."""
    a = cont_frac_sqrt(D)
    a_rpt = a[1:]
    M = len(a_rpt)

    num = [0,1,a[0]]
    denom = [1,0,1]

    n = 3
    while True:
        num.append(a_rpt[(n - 3) % M]*num[n-1] + num[n-2])
        denom.append(a_rpt[(n - 3) % M]*denom[n-1] + denom[n-2])
        if num[-1]**2 - D * denom[-1]**2 == 1:
            break
        else:
            n += 1

    return (num[-1], denom[-1])

minimal_x_values = []
for D in range(1001):
    if sqrt(D).is_integer() == True:
        minimal_x_values.append(0)
    else:
        minimal_x_values.append(find_minimal_Pell_solution(D)[0])

maximal_x = max(minimal_x_values)
print(minimal_x_values.index(maximal_x), maximal_x)

