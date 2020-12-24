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
    tmap = {}
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
        tmap[l] = tiles.count(l) % 2 == 1
    print(tmap)
    print(sum(1 for l, v in tmap.items() if v))

    neighs = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]
    for d in range(100):
        creates = []
        for x, y in tmap.keys():
            for dx, dy in neighs:
                target = (x + dx, y + dy)
                if target not in tmap:
                    creates.append(target)
        for tile in creates:
            tmap[tile] = False
        updates = []
        for tile, state in tmap.items():
            # black = True
            black_neighs = 0
            for dx, dy in neighs:
                x, y = tile
                target = (x + dx, y + dy)
                tst = tmap.get(target, False)
                if tst:
                    black_neighs += 1
            if state:
                if black_neighs == 0 or black_neighs > 2:
                    updates.append(tile)
            else:
                if black_neighs == 2:
                    updates.append(tile)
        for upd in updates:
            tmap[upd] = not tmap[upd]
        print(sum(1 for l, v in tmap.items() if v))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
