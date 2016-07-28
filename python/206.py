# Project Euler 206

desired = '1_2_3_4_5_6_7_8_9_0'

for n in range(10**9,10**10,10):
    if str(n**2)[::2] == desired[::2]:
        print(n)
        break

# 1389019170