# Project Euler 68

import itertools as it
from math import factorial

base_permutations = list(it.permutations(range(1,10)))

def Magic5GonString(x):
    """Generate the string associated to a magic 5-gon.
    Input is a permutation."""
    y = [10] + list(x)

    # Starting from the horizontal node in the picture, moving inward.
    magic_5_gon = (
        (y[0], y[1], y[2]),
        (y[3], y[2], y[4]),
        (y[5], y[4], y[6]),
        (y[7], y[6], y[8]),
        (y[9], y[8], y[1])
        )

    # check to see if the 5-gon is "magic"
    if sum(list(magic_5_gon[0])) \
        == sum(list(magic_5_gon[1])) \
        == sum(list(magic_5_gon[2])) \
        == sum(list(magic_5_gon[3])) \
        == sum(list(magic_5_gon[4])):

        outside_nodes = [y[0], y[3], y[5], y[7], y[9]]

        min_index = outside_nodes.index(min(outside_nodes))

        string = ''
        for j in range(min_index, min_index + 5):
            for k in [0,1,2]:
                string += str(magic_5_gon[j % 5][k])

        return int(string)

    # if the 5-gon isn't "magic", return 0
    else:
        return 0

max_digit_string = 0

for x in base_permutations:
    n = Magic5GonString(x)
    if n >= max_digit_string:
        max_digit_string = n

print(max_digit_string) # 6531031914842725

