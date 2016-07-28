# Project Euler 57

from fractions import Fraction

N = 10**3

numerators = [0,1,1]
denominators = [1,0,1]

for n in range(3,N+3):
    numerators.append(2*numerators[n-1] + numerators[n-2])
    denominators.append(2*denominators[n-1] + denominators[n-2])

count = 0

for n in range(3,N+3):
    if len(str(numerators[n])) > len(str(denominators[n])):
        count += 1

print(count) # 153