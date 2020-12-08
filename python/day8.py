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

def run(insts):
    inst_execs = [0] * len(insts)
    acc = 0
    pc = 0
    while True:
        if pc >= len(insts):
            break
        inst, arg = insts[pc]
        print(inst, arg)
        inst_execs[pc] += 1
        if inst_execs[pc] >= 2:
            break
        if inst == "acc":
            acc += arg
            pc += 1
        elif inst == "jmp":
            pc += arg
        elif inst == "nop":
            pc += 1

    print(acc)

insts = []
for l in lines:
    inst, arg = l.split()
    insts.append((inst, int(arg)))

    if False:
        total += 1

run(insts)



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
