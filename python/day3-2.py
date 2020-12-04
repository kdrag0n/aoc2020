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
result = 1

for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    total = 0
    x = 0
    y = 0
    while True:
        if tmap[y][x] == "#":
            total += 1

        x += slope[0]
        y += slope[1]

        if x >= len(tmap[0]) or y >= len(tmap):
            break

    result *= total



print(f"Total: {total}")
print(f"Result: {result}")
print(f"2: {0}")
