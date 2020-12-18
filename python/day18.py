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

insts = []
def eval_block(b, init_lhs=None, evi=1):
    i=0
    op=None
    lhs = init_lhs
    rhs = None
    while i < len(b):
        c = b[i]
        match = re.search(r"^(\d+)", b[i:])
        if match:
            n = int(match.group(1))
            i += len(match.group(1))

            if lhs is None:
                lhs = n
            else:
                rhs = n
                olhs = lhs
                if op == "*":
                    lhs *= rhs
                elif op == "+":
                    lhs += rhs
                elif op == "-":
                    lhs -= rhs
                elif op == "/":
                    lhs /= rhs
                print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
                op=None
                #lhs = rhs
                rhs = None
            continue
        
        if c in "*+-/":
            op = c
            
        elif c == "(":
            opres, chars = eval_block(b[i+1:], evi=evi+1)
            i += chars + 1
            if lhs is None:
                lhs = opres
            else:
                rhs = opres
                olhs = lhs
                if op == "*":
                    lhs *= rhs
                elif op == "+":
                    lhs += rhs
                elif op == "-":
                    lhs -= rhs
                elif op == "/":
                    lhs /= rhs
                print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
                op=None
                #lhs = rhs
                rhs = None
        elif c == ")":
            break
        i += 1
    print()
    return lhs, i

for l in lines:
    l = l.replace(" ", "")
    print(eval_block(f"({l})"))
    total += eval_block(f"({l})")[0]




print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
