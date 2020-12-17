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
    vnearby = []
    for nt in nearby:
        valid = True
        for val in nt:
            val_valid = False
            for rn, rule in rules.items():
                for minb, maxb in rule:
                    print("-", val, minb, maxb)
                    if val >= minb and val <= maxb:
                        val_valid = True
                        print(val)
                    if val_valid:
                        break
                if val_valid:
                    break
            
            print(val_valid)
            if not val_valid:
                valid = False
                break
        if valid:
            vnearby += [nt]
    
    vnearby += [cur]
    print('VV', vnearby)
    fns = {}
    for fi in range(len(vnearby[0])):
        print("\n\n\nFI", fi)
        for fn, ruless in rules.items():
            print(fn, ruless)
            fr_val_cnt = 0
            for nt in vnearby:
                val = nt[fi]
                print(" > nt", nt, "vv", val)
                val_valid = False
                for minb, maxb in ruless:
                    print("     val", val, "min", minb, "max", maxb)
                    if val >= minb and val <= maxb:
                        val_valid = True
                        print("       valid")
                        break
                
                print(" >", val_valid)
                if val_valid:
                    fr_val_cnt += 1
            
            print(' val', fr_val_cnt)
            if fr_val_cnt == len(vnearby) and fn not in fns.values():
                fns[fi] =fn
                break
    
    a = 1
    for fi, fn in fns.items():
        if fn.startswith("departure"):
            print(fn)
            a *= cur[fi]
    print(fns)

    print("\n", inval)
    print("\n\n\n", a)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
