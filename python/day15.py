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
    num_occurs = []
    num_turns = {}
    for turn in range(2020):
        if turn < len(starts):
            num = starts[turn]
        elif num_occurs.count(num) == 1:
            num = 0
        else:
            last_spk = (num_turns[num][-1] + 1)
            last_last_spk = (num_turns[num][-2] + 1)
            num = last_spk - last_last_spk
        last_num = num
        num_occurs.append(num)
        if num in num_turns:
            num_turns[num] += [turn]
        else:
            num_turns[num] = [turn]

    print(num)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
