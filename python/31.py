# -*- coding: utf-8 -*-
# Project Euler 31

# very ugly

def TotalUp(a,b,c,d,e,f,g,h):
    return a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h

count = 0

for h in range(2):
    for g in range(3 - TotalUp(0,0,0,0,0,0,0,h)//100):
        for f in range(5 - TotalUp(0,0,0,0,0,0,g,h)//50):
            for e in range(11 - TotalUp(0,0,0,0,0,f,g,h)//20):
                for d in range(21 - TotalUp(0,0,0,0,e,f,g,h)//10):
                    for c in range(41 - TotalUp(0,0,0,d,e,f,g,h)//5):
                        for b in range(101 - TotalUp(0,0,c,d,e,f,g,h)//2):
                            for a in range(201 - TotalUp(0,b,c,d,e,f,g,h)):
                                if TotalUp(a,b,c,d,e,f,g,h) == 200:
                                    count += 1

print(count) # 73682; 3 seconds

# better way using dynamic programming

value = 200 # total sought
count = [0]*(value+1) # building a list
count[0] = 1
coins = [1,2,5,10,20,50,100,200]

for x in coins:
    for i in range(x, value+1):
        count[i] += count[i-x]
print(count[value]) # 0.1 seconds

