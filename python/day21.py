#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0
import collections
while True:
    pos_algs = collections.defaultdict(list)
    all_ings = set()
    all_ings_list = []
    for l in lines:
        l1, l2 = l.replace(")", "").split(" (contains ")
        ings = l1.split(" ")
        for i in ings:
            all_ings.add(i)
            all_ings_list += [i]
        algs = l2.split(", ")
        for alg in algs:
            pos_algs[alg] += [set(ings)]
    alg_commons = set()
    for alg, ingsets in pos_algs.items():
        s = ingsets[0]
        for s2 in ingsets[1:]:
            s = s.intersection(s2)
        common = s
        print(alg, common)
        alg_commons.update(common)
    not_algs = all_ings - alg_commons
    print(not_algs)
    for ing in not_algs:
        total += all_ings_list.count(ing)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
