#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr if i]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0
def cscore(cs):
    sc = 0
    for i, c in enumerate(reversed(cs)):
        sc += c * (i+1)
    return sc
while True:
    p1c = ints(lines[0].split("\n")[1:])
    p2c = ints(lines[1].split("\n")[1:])

    while p1c and p2c:
        c1 = p1c.pop(0)
        c2 = p2c.pop(0)

        if c1 > c2:
            p1c += [c1, c2]
        else:
            p2c += [c2, c1]
    if p1c:
        total = cscore(p1c)
    elif p2c:
        total = cscore(p2c)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
