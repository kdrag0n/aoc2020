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
    pos_algs2 = {}
    for alg, ingsets in pos_algs.items():
        s = ingsets[0]
        for s2 in ingsets[1:]:
            s = s.intersection(s2)
        common = s
        print(alg, common)
        alg_commons.update(common)
        pos_algs2[alg] = common
    not_algs = all_ings - alg_commons
    print(not_algs)
    for ing in not_algs:
        total += all_ings_list.count(ing)
    # pass2
    sure_maps = {}
    print(pos_algs2)
    while any(len(s) > 0 for s in pos_algs2.values()):
        for alg, ingset in pos_algs2.items():
            if len(ingset) == 1:
                sure_maps[alg] = [*ingset][0]
        print('sure-----', sure_maps)
        for alg, ingset in pos_algs2.items():
            ingset -= set(sure_maps.values())
            print(alg, ingset)
        print()
        #for alg, ingset in pos_algs2.items():
        #    newset = ingset
        #    for alg2, ingset2 in pos_algs2.items():
        #        if alg2 != alg:
        #            newset -= ingset2
        #            print(alg, '::', alg2, ingset2, '->', newset)
        #    print(alg, newset)
    alp = sorted(sure_maps.items(), key=lambda t:t[0])
    print(",".join(v[1] for v in alp))
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
