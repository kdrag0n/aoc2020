#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [int(l) for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

while True:
    lines.append(max(lines) + 3)
    lines.sort()
    last_j = 0
    diffs = []
    arrgs = 0
    for j in lines:
        if j > last_j and j <= last_j + 3:
            arrgs += 1
            print(j)
            diffs += [j - last_j]
            last_j = j
            print(diffs)

    jd1 = sum(1 for i in diffs if i == 1)
    jd3 = sum(1 for i in diffs if i == 3)
    print(jd1* jd3)
    print('a', arrgs)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
