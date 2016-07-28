# Project Euler 58

from eulertools import IsPrime1

def percentage_test(a,b):
    if 0 < len(a) / len(b) < 0.1:
        return True
    else:
        return False

diagonal_entries = [1]
prime_diagonal_entries = []

N = 1

while not percentage_test(prime_diagonal_entries, diagonal_entries):
    for j in range(4):
        entry = diagonal_entries[-1] + 2*N
        diagonal_entries.append(entry)
        if IsPrime1(entry):
            prime_diagonal_entries.append(entry)
    N += 1

print(2*N-1) # 26241