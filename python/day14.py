#!/usr/bin/env python3

import sys
import re
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
    mem = {}
    for l in lines:
        print(l)
        if "mask" in l:
            rmask = l.split()[2]
            mask = []
            for i, c in enumerate(rmask[::-1]):
                if c != "X":
                    mask.append((i, c))
            continue
        match = re.match(r"^mem\[(\d+)\] = (.+)$", l)
        addr = int(match.group(1))
        val = int(match.group(2))

        for bit, bval in mask:
            if bval == "1":
                val |= (1 << bit)
            else:
                val &= ~(1 << bit)

        mem[addr] = val

    print(mem)
    print(sum(mem.values()))
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
