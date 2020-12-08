#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

last_acc=0
def run(insts):
    inst_execs = [0] * len(insts)
    global last_acc
    acc = 0
    pc = 0
    last_nop_jmp = -1
    succ = True
    while True:
        if pc >= len(insts):
            break
        inst, arg = insts[pc]
        print(inst, arg)
        inst_execs[pc] += 1
        if inst_execs[pc] >= 50:
            #if inst == "jmp":
            #    inst = "nop"
            #elif inst == "nop":
            #    inst = "jmp"
            #else:
            #    print(last_nop_jmp)
            #    _inst, _arg = insts[last_nop_jmp]
            #    if _inst == "jmp":
            #        _inst = "nop"
            #    elif _inst == "nop":
            #        _inst = "jmp"
            #    else:
            #        print("EEEEEEEEEEEEE")
            #    print('change:', last_nop_jmp, _inst, _arg)
            #    insts[last_nop_jmp] = (_inst, _arg)
            #    print(inst)
            #print("==============================")
            #insts[pc] = (inst, arg)
            #print(acc)
            succ = False
            break
        if inst == "acc":
            acc += arg
            pc += 1
        elif inst == "jmp":
            last_nop_jmp = pc
            pc += arg
        elif inst == "nop":
            last_nop_jmp = pc
            pc += 1

    print(acc)
    last_acc=acc
    return succ

insts = []
for l in lines:
    inst, arg = l.split()
    insts.append((inst, int(arg)))

    if False:
        total += 1

#run(insts)
#run(insts)
for i, (inst, arg) in enumerate(insts):
    print(i)
    insts2 = insts.copy()
    if inst == "nop":
        insts2[i] = ("jmp", arg)
    elif inst == "jmp":
        insts2[i] = ("nop", arg)
    else:
        continue
    #print(run(insts2))
    x = run(insts2)
    print(x)
    if x:
        print("insts2 ok", last_acc)
        break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
