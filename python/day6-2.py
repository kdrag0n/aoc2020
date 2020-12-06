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
    ans = []
    for l in lines:
        print(l)
        if not l:
            if len(ans)<1:
                ans=[set()]
            v = ans[0]
            for s in ans:
                v = s.intersection(v)
            v = len(v)
            grps.append(v)
            print(v)
            total+=v
            ans=[]
            continue
        asd=set()
        for c in l:
            asd.add(c)
        ans+=[asd]


        if False:
            total += 1

    break


print(sum(grps))
print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
