#!/usr/bin/env python3

import sys

pa_len=25

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
    for i, l in enumerate(lines):
        print('eval', l)
        if i < pa_len:
            continue
        print('cand', lines[i-pa_len:i])
        valid = False
        for vx in lines[i-pa_len:i]:
            for vy in lines[i-pa_len:i]:
                if vx == vy:
                    continue
                    
                if vx + vy == l:
                    valid = True
                    break
            
            if valid:
                break
        
        if not valid:
            print('nv', l)
            exit(1)

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
