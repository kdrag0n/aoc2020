#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n")]
    lines+=[""]



ilist = []
imap = {}

total = 0
result = 0
other = 0

while True:
    grps=[]
    ans = set()
    for l in lines:
        print(l)
        if not l:
            grps.append(len(ans))
            print(len(ans))
            total+=len(ans)
            ans=set()
            continue
        for c in l:
            ans.add(c)


        if False:
            total += 1

    break


print(sum(grps))
print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
