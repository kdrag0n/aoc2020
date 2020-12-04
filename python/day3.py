#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

tmap = []
with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]
    for line in lines:
        tmap.append(list(line) * 5000)



total = 0
result = 0

x = 0
y = 0
while True:
    if tmap[y][x] == "#":
        total += 1

    x += 3
    y += 1

    if x >= len(tmap[0]) or y >= len(tmap):
        break




print(f"Total: {total}")
print(f"Result: {result}")
print(f"2: {0}")
