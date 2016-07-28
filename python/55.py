# Project Euler 55

N = 10**4
M = 50

Lychrel_numbers = []

def is_pallindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

for x in range(1,N):
    test = x + int(str(x)[::-1])
    iteration = 0
    while not is_pallindrome(test):
        if iteration < 51:
            iteration += 1
            test = test + int(str(test)[::-1])
        else:
            Lychrel_numbers.append(x)
            break

print(len(Lychrel_numbers))


