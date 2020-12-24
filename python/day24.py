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
    lcs = {}
    tiles = []
    for l in lines:
        x = 0
        y = 0
        l = l.replace("se", "$").replace("sw", "S").replace("nw", "!").replace("ne", "N")
        print(l)
        for inst in list(l):
            if inst == "e":
                x += 1
            elif inst == "$":
                x += 1
                y -= 1
            elif inst == "S":
                y -= 1
            elif inst == "w":
                x -= 1
            elif inst == "!":
                y += 1
                x -= 1
            elif inst == "N":
                y += 1
        tiles.append((x, y))
    for l in tiles:
        lcs[l] = tiles.count(l)
    print(lcs)
    print(sum(1 for l, v in lcs.items() if v % 2 == 1))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
