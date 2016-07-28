# Project Euler 80

from decimal import *
from math import sqrt

getcontext().prec = 102

def hundred_digit_sum(x):
    """Returns the sum of the first hundred digits following the decimal
    point."""
    y = str(x)
    decimal_point_index = y.index('.')
    z = y[:decimal_point_index] + y[decimal_point_index+1:]
    the_sum = 0
    for n in z[:100]:
        the_sum += int(n)
    return the_sum

non_square_naturals = [n for n in range(1,101) if not sqrt(n).is_integer()]

total_sum = 0
for n in non_square_naturals:
    total_sum += hundred_digit_sum(Decimal(n).sqrt())

print(total_sum) # 40886





