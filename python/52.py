# Project Euler 52

M = 6

def same_digit_test(x):
    digits = {d for d in str(x)}
    for m in range(1,M+1):
        if {d for d in str(m*x)} != digits:
            return False
    return True

N = 6

for n in range(1,10**N):
    if same_digit_test(n):
        print(n)
        break

# 142857