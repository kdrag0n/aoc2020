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

def trx(n, ls):
    v = 1
    for i in range(ls):
        v *= n
        v = v % 20201227
    return v

while True:
    ckey, dkey = ints(lines)
    cls = -1
    dls = -1

    v = 1
    for cand in range(1, 10000001):
        v = (v * 7) % 20201227
        if cand % 10000 == 0:
            print(cand)
        if cls == -1 and v == ckey:
            print('cls', cand, v)
            cls = cand
        elif dls == -1 and v == dkey:
            print('dls', cand, v)
            dls = cand
    print('lss', cls, dls)
    print(trx(dkey, cls))
    print(trx(ckey, dls))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
