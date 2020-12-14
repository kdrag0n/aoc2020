#!/usr/bin/env python3

import sys
import itertools
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
addrs = []
def rec_x(mask, maski):
    global addrs
    global mem
    for i in range(maski, len(mask)):
        bit, bval = mask[i]
        if bval == "X":
            new = []
            for addr in addrs:
                addr2 = addr | (1 << bit)
                mem[addr2] = val
                new += [addr2]
                addr2 = addr & ~(1 << bit)
                mem[addr2] = val
                new += [addr2]
            addrs += new

            print([bin(z) for z in addrs])
            rec_x(mask, i+1)

while True:
    mem = {}
    for l in lines:
        print(l)
        if "mask" in l:
            rmask = l.split()[2]
            mask = []
            for i, c in enumerate(rmask[::-1]):
                mask.append((i, c))
            continue
        match = re.match(r"^mem\[(\d+)\] = (.+)$", l)
        addr = int(match.group(1))
        val = int(match.group(2))

        addrs = []
        for bit, bval in mask:
            if bval == "1":
                addr |= (1 << bit)
        print(list(itertools.product([0, 1], repeat="".join(k[1] for k in mask).count("X"))))
        for comb in itertools.product([0, 1], repeat="".join(k[1] for k in mask).count("X")):
            addr2 = addr
            mask2_tmp = []
            xb = 0
            for bit, bval in mask:
                if bval == "X":
                    mask2_tmp.append((bit, comb[xb]))
                    xb+= 1
            
            for bit, bval in mask2_tmp:
                if bval == 1:
                    addr2 |= (1 << bit)
                else:
                    addr2 &= ~(1 << bit)
            
            addrs.append(addr2)
        
        for addr in addrs:
            print(bin(addr))
            mem[addr] = val

    print(mem)
    print(sum(mem.values()))
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
