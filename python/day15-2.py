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

while True:
    starts = list(map(int, lines[0].split(",")))
    last_num = -1
    num_occurs = {}
    num_turns = {}
    for turn in range(30000000):
        if turn%1000 == 0:
            print(turn)
        if turn < len(starts):
            num = starts[turn]
        elif num in num_occurs and num_occurs[num] == 1:
            num = 0
        else:
            last_spk = (num_turns[num][-1] + 1)
            last_last_spk = (num_turns[num][-2] + 1)
            num = last_spk - last_last_spk
        last_num = num
        if num in num_occurs:
            num_occurs[num] += 1
        else:
            num_occurs[num] = 1
        if num in num_turns:
            nt = num_turns[num]
            nt[0] = nt[1]
            nt[1] = turn
        else:
            num_turns[num] = [-1, turn]

    print()
    print(num)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
