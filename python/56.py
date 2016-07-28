# Project Euler 56

N = 100

sum_list = []

for a in range(1,N):
    for b in range(1,N):
        x = a**b
        digit_sum = 0
        for d in str(x):
            digit_sum += int(d)
        sum_list.append(digit_sum)

print(max(sum_list)) # 972
