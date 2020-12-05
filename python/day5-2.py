#!/usr/bin/env python3

import sys
import re
import math


def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

while True:
    
    for l in lines:
        r1 = 0
        r2 = 127
        lastr=""
        c1=0
        c2=7
        lastc=""
        for c in l:
            print(c)
            if c == "F":
                r1 = r1
                r2 = int(math.floor(((r1+r2)/2)))
                lastr=c
            elif c=="B":
                r1 = int(math.ceil(((r1+r2)/2)))
                r2 = r2
                lastr=c
            elif c=="R":
                c1 = int(math.ceil(((c1+c2)/2)))
                c2 = c2
                lastc=c
            elif c=="L":
                c1 = c1
                c2 = int(math.floor(((c1+c2)/2)))
                lastc=c

            print('r',r1,r2)
            print('c',c1,c2)
        if lastr=="F":
            fr=r1
        else:
            fr=r2
        if lastc=="L":
            fc=c1
        else:
            fc=c2
        print(fr*8+fc)
        ilist.append(fr*8+fc)
        if False:
            total += 1

    break

miss=[]
for r in range(128):
    for c in range(8):
        iri=r*8+c
        if iri not in ilist:
            miss.append(iri)
            print("MIS", iri)

for m in miss:
    if m-1 in ilist and m+1 in ilist:
        print("MMMM", m)
print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {max(ilist)}")
