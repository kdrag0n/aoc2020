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

def val(seq):
    last_j = 0
    for j in seq:
        if not (j > last_j and j <= last_j + 3):
            return False
        last_j = j
    return True

#arrgs = set()
def search(cont):
    #global arrgs
    arrgs = 0
    last_j = cont[0]
    for i in range(1, len(cont)):
        j = cont[i]
        if j > last_j and j <= last_j + 3:
            print(j, cont)
            arrgs += search(cont[i:])
            print('rec')
        else:
            break
    return arrgs

while True:
    lines.append(0)
    lines.append(max(lines) + 3)
    lines.sort()
    last_j = 0
    diffs = []
    arrgs =search(lines)

    print('a', arrgs)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
