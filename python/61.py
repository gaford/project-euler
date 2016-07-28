# Project Euler 61

import itertools

def polygonal(s,n):
    """Returns the nth s-gonal number."""
    return (n**2 * (s - 2) - n * (s - 4)) // 2

"""Determine the relevant s-gonal numbers."""

# for s in range(3,9):
#     n = 0
#     x = polygonal(s,n)
#     while x < 1000:
#         n += 1
#         x = polygonal(s,n)
#     else:
#         print("The first %s-gonal four-digit number is the %s-th." % (s,n))
#     while x < 10000:
#         n += 1
#         x = polygonal(s,n)
#     else:
#         print("The last %s-gonal four-digit number is the %s-th." % (s,n-1))

"""Relevant polygonal numbers."""

triagonals = [polygonal(3,n) for n in range(45,142)]
squares = [polygonal(4,n) for n in range(32,101)]
pentagonals = [polygonal(5,n) for n in range(26,83)]
hexagonals = [polygonal(6,n) for n in range(23,70)]
heptagonals = [polygonal(7,n) for n in range(21,65)]
octagonals = [polygonal(8,n) for n in range(19,60)]

"""Building the cycle."""

def digit_compare(a,b):
    return str(a)[2:] == str(b)[:2]

polygonal_numbers = [
    triagonals, squares, pentagonals, hexagonals, heptagonals, octagonals
]

for permutation in list(itertools.permutations(range(6))):

    dict0 = {}
    for a in polygonal_numbers[permutation[0]]:
        dict0[a] = set()
        for b in polygonal_numbers[permutation[1]]:
            if digit_compare(a,b):
                dict0[a] = dict0[a] | {b}

    dict1 = {}
    for a in polygonal_numbers[permutation[1]]:
        dict1[a] = set()
        for b in polygonal_numbers[permutation[2]]:
            if digit_compare(a,b):
                dict1[a] = dict1[a] | {b}

    dict2 = {}
    for a in polygonal_numbers[permutation[2]]:
        dict2[a] = set()
        for b in polygonal_numbers[permutation[3]]:
            if digit_compare(a,b):
                dict2[a] = dict2[a] | {b}

    dict3 = {}
    for a in polygonal_numbers[permutation[3]]:
        dict3[a] = set()
        for b in polygonal_numbers[permutation[4]]:
            if digit_compare(a,b):
                dict3[a] = dict3[a] | {b}

    dict4 = {}
    for a in polygonal_numbers[permutation[4]]:
        dict4[a] = set()
        for b in polygonal_numbers[permutation[5]]:
            if digit_compare(a,b):
                dict4[a] = dict4[a] | {b}

    dict5 = {}
    for a in polygonal_numbers[permutation[5]]:
        dict5[a] = set()
        for b in polygonal_numbers[permutation[0]]:
            if digit_compare(a,b):
                dict5[a] = dict5[a] | {b}

    for a in polygonal_numbers[permutation[0]]:
        for b in dict0[a]:
            for c in dict1[b]:
                for d in dict2[c]:
                    for e in dict3[d]:
                        for f in dict4[e]:
                            if a in dict5[f]:
                                print(a, b, c, d, e, f, a + b + c + d + e + f)

# 28684




