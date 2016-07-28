# Project Euler 60

from eulertools import Sieve, IsPrime1

def prime_concatenate(p,q):
    return IsPrime1(int(str(p) + str(q))) and IsPrime1(int(str(q) + str(p)))

primes = Sieve(10**4)

candidates_dict = {}
for j in range(len(primes)):
    for k in range(j+1,len(primes)):
        p = primes[j]
        q = primes[k]
        if prime_concatenate(p,q):
            try:
                candidates_dict[p] = candidates_dict[p] | {q}
            except KeyError:
                candidates_dict[p] = {q}
            try:
                candidates_dict[q] = candidates_dict[q] | {p}
            except KeyError:
                candidates_dict[q] = {p}

good_primes = sorted(list(candidates_dict.keys()))

results = []
for p1 in good_primes:
    for p2 in candidates_dict[p1]:
        set3 = candidates_dict[p1] & candidates_dict[p2]
        if set3:
            for p3 in set3:
                set4 = set3 & candidates_dict[p3]
                if set4:
                    for p4 in set4:
                        set5 = set4 & candidates_dict[p4]
                        if set5:
                            for s in set5:
                                result = sorted({p1,p2,p3,p4} | {s})
                                if result not in results:
                                    results.append(result)
                                    print(result)

results_sums = [sum(result) for result in results]

print("The minimum sum is %s." % min(results_sums))

# 45.5 seconds, [13, 5197, 5701, 6733, 8389]

""" OLD CODE """

# """Detecting commuting primes up to the sieve limit."""

# pre_candidates = []

# for p in primes:
#     p_string = str(p)
#     for j in range(1,len(p_string)):
#         if IsPrime1(int(p_string[:j])) and IsPrime1(int(p_string[j:])) \
#             and not p_string[:j].startswith('0') \
#             and not p_string[j:].startswith('0'):
#             pre_candidates.append(sorted([int(p_string[:j]), \
#                 int(p_string[j:])]))

# """Sorting the commuting primes."""

# pre_candidates_sorted = sorted(pre_candidates, key = lambda x :  (x[0], x[1]))

# candidates = []
# for j in range(len(pre_candidates_sorted)-1):
#     if pre_candidates_sorted[j] == pre_candidates_sorted[j+1]:
#         candidates.append(pre_candidates_sorted[j])

# """Building a dictionary of primes which commute with each other."""

# candidates_dict = {}
# for j in range(len(candidates)):
#     try:
#         # candidates_dict[candidates[j][0]].append(candidates[j][1])
#         candidates_dict[candidates[j][0]] = candidates_dict[candidates[j][0]] \
#             | {candidates[j][1]}
#     except KeyError:
#         candidates_dict[candidates[j][0]] = {candidates[j][1]}
#     try:
#         candidates_dict[candidates[j][1]] = candidates_dict[candidates[j][1]] \
#             | {candidates[j][0]}
#     except KeyError:
#         candidates_dict[candidates[j][1]] = {candidates[j][0]}

