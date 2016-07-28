# Project Euler 145

odd_digits = '13579'

def reverse(n):
    return int(str(n)[::-1])

def reversible(n):
    if n % 10 == 0:
        return False
    else:
        x = n + reverse(n)
        for char in str(x):
            if char not in odd_digits:
                return False
        return True

count = 0
for n in range(1,10**3):
    if reversible(n):
        count += 1

print(count)






