#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l.split("\n") for l in f.read().split("\n\n")]



ilist = []
imap = {}

total = 0
result = 0
other = 0

while True:
    rules = {}
    cur = []
    nearby = []
    for sec in lines:
        if sec[0] == "your ticket:":
            cur = [int(v) for v in sec[1].split(",")]
        elif sec[0] == "nearby tickets:":
            for l in sec[1:]:
                if l:
                    nearby += [[int(v) for v in l.split(",")]]
        elif sec[0] == "":
            pass
        else:
            for l in sec:
                k, vss = l.split(": ")
                vs = vss.split(" or ")
                rules[k] = [[int(x) for x in va.split("-")] for va in vs]
    print(rules)
    print(cur)
    print(nearby)
    print()
    inval = 0
    for nt in nearby:
        for val in nt:
            valid = False
            for rn, rule in rules.items():
                for minb, maxb in rule:
                    print("-", val, minb, maxb)
                    if val >= minb and val <= maxb:
                        valid = True
                        print(val)
                    if valid:
                        break
                if valid:
                    break
            
            print(valid)
            if not valid:
                inval += val

    print("\n", inval)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
