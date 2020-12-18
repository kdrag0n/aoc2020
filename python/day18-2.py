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

#insts = []
#def parse_block(b, init_lhs=None, evi=1, nested_insts=None):
#    i=0
#    op=None
#    lhs = init_lhs
#    rhs = None
#    while i < len(b):
#        c = b[i]
#        match = re.search(r"^(\d+)", b[i:])
#        if match:
#            n = int(match.group(1))
#            i += len(match.group(1))
#
#            if lhs is None:
#                lhs = n
#                nested_insts.append(lhs)
#            else:
#                rhs = n
#                olhs = lhs
#                nested_insts.append(rhs)
#                nested_insts.append(op)
#                print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
#                op=None
#                #lhs = rhs
#                rhs = None
#            continue
#        
#        if c in "*+-/":
#            op = c
#            
#        elif c == "(":
#            ni = []
#            nested_insts.append(ni)
#            opres, chars = parse_block(b[i+1:], evi=evi+1, nested_insts=ni)
#            i += chars + 1
#            if lhs is None:
#                lhs = opres
#            else:
#                rhs = opres
#                olhs = lhs
#                nested_insts.append(rhs)
#                nested_insts.append(op)
#                print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
#                op=None
#                #lhs = rhs
#                rhs = None
#        elif c == ")":
#            break
#        i += 1
#    print()
#    return lhs, i
#def eval_block(insts, evi=1):
#    #p1
#    lhs=None
#    rhs=None
#
#    new_insts = []
#    for inst in insts:
#        print("I", inst)
#        nval = None
#        op=None
#        if isinstance(inst, list):
#            nval = eval_block(inst, evi=evi+1)
#        elif isinstance(inst, str):
#            op = inst
#        elif isinstance(inst, int):
#            nval = inst
#        
#        if nval is not None:
#            if lhs is None:
#                lhs = nval
#            else:
#                rhs = nval
#        if op is not None:
#            olhs = lhs
#            if op == "+":
#                lhs += rhs
#                print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
#            else:
#                new_insts += [lhs]
#                new_insts += [rhs, op]
#                print(f"{'    ' * evi} [*] {lhs} {op}")
#            op=None
#            #lhs = rhs
#            rhs = None
#    
#    #p2
#    print("_ni", new_insts)
#    for inst in new_insts:
#        print("NI", inst)
#        nval = None
#        op=None
#        if isinstance(inst, list):
#            nval = eval_block(inst, evi=evi+1)
#        elif isinstance(inst, str):
#            op = inst
#        elif isinstance(inst, int):
#            nval = inst
#        
#        if nval is not None:
#            if lhs is None:
#                lhs = nval
#            else:
#                rhs = nval
#        if op is not None:
#            olhs = lhs
#            if op == "*":
#                lhs *= rhs
#            else:
#                new_insts += [lhs, op]
#            rhs = None
#            print(f"{'    ' * evi}{olhs} {op} {rhs} = {lhs}")
#            op=None
#            #lhs = rhs
#            rhs = None
#    print()
#    return lhs
#for l in lines:
#    l = l.replace(" ", "")
#    insts = []
#    s, c = parse_block(f"({l})", nested_insts=insts)
#    print(s, c)
#    print(insts)
#    s = eval_block(insts)
#    print(s)
#    total += s


class oint:
    def __init__(self, n):
        self.n = n
    def __add__(self, b):
        return oint(self.n * b.n)
    def __mul__(self, b):
        return oint(self.n + b.n)

for l in lines:
    l = l.replace(" ", "")
    insts = []
    ois = re.sub(r"(\d+)", r"oint(\1)", l)
    final = ois.replace("+", "ZZ").replace("*", "+").replace("ZZ", "*")
    print(final)
    s = eval(final)
    total += s.n
    print(s)



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
