#!/usr/bin/env python3

import sys
import re
def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [[l for l in y.split("\n") if l] for y in f.read().replace("8: 42", "8: 42 | 42 8").replace("11: 42 31", "11: 42 31 | 42 11 31").split("\n\n") if y]



ilist = []
imap = {}

total = 0
result = 0
other = 0
def lmatch(l, rset, i=0):
    print("lmatch", rset)
    for c in l[i:]:
        print('char', c)
        lpassed = False
        bstarti = i
        for branch in rset:
            i = bstarti
            print('branch', branch)
            bpassed = True
            for r in branch:
                print('rule', r)
                rpassed = False
                if isinstance(r, str):
                    print(f'    check str {r}')
                    if c == r:
                        rpassed = True
                if isinstance(r, int):
                    print(f'    check intref {r}')
                    if isinstance(rs[r], str):
                        print(f'    check intref str {rs[r]}')
                        if c == rs[r]:
                            rpassed = True
                    else:
                        print(f'    check intref lmatch {rs[r]}')
                        lmpassed, si = lmatch(l, rs[r], i)
                        if lmpassed:
                            rpassed = True
                            i = si
                print(f'    pass {rpassed}')
                if rpassed:
                    i += 1
                    c = l[i]
                else:
                    bpassed = False
                    break
            if bpassed:
                break
            else:
                continue
        if not bpassed:
            return False, i
        
    return True, i
def make_re():
    rz = "\n".join(lines[0])
    last_rz = rz
    iters = 0
    while re.search(r"\d", re.sub(r"^\d+: ", "", rz)):
        print(rz)
        print()
        dd = dict(tuple(l.split(": ")) for l in rz.split("\n"))
        for n, r in dd.items():
            keys = [z.split(": ")[0] for z in rz.split("\n")]
            jvals = "\n".join([z.split(": ")[1] for z in rz.split("\n")])
            nvals = re.sub(f"\\b{n}\\b", f"({r})", jvals).split("\n")
            nrz = []
            print(rz)
            print()
            for i, k in enumerate(keys):
                nrz.append(f"{k}: {nvals[i]}")
            rz = "\n".join(nrz)
        if last_rz == rz:
            break
        last_rz = rz
        iters += 1
        if iters >= 5:
            break
    rz = rz.replace('"', '').replace(' ', "")
    print(rz)
    regs = dict(tuple(l.split(":")) for l in rz.split("\n"))
    reg = "^" + regs["0"] + "$"
    print(reg)
    return reg
while True:
    reg = make_re()
    for l in lines[1]:
        m = re.match(reg, l)
        
        print(l, m)
        if m:
            total += 1
    #rs = {}
    #for rl in lines[0]:
    #    nl, rrl = rl.split(": ")
    #    segs = rrl.split(" | ")
    #    rlv = []
    #    for rc in segs:
    #        if rc[0] == '"' and rc[2] == '"' and len(rc) == 3:
    #            rlv = rc[1]
    #        else:
    #            v = [int(x) for x in rc.split(" ")]
    #            rlv.append(v)
    #    
    #    rs[int(nl)] = rlv
    #for l in lines[1]:
    #    print(l, lmatch(l, rs[0]))
    #    print()
    #    print()
    #    print()
    #    print()
    #    print()
    #    print()
    #    exit()

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
