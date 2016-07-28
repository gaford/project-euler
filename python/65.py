# Project Euler 65

from fractions import Fraction

N = 10**2

c_frac_terms = [0,0,2,1,2]
for j in range(2,(N+1)//2):
    c_frac_terms.extend([1,1,2*j])

numerators = [0,1]
denominators = [1,0]

for n in range(2,N+3):
    numerators.append(c_frac_terms[n]*numerators[n-1] + numerators[n-2])
    denominators.append(c_frac_terms[n]*denominators[n-1] + denominators[n-2])

print(sum([int(d) for d in str(numerators[N+1])])) # 272


