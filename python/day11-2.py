#!/usr/bin/env python3

import sys
import copy

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [list(l) for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0
rounds=0
def simround():
    global rounds
    updates = []
    for y, row in enumerate(lines):
        for x, seat in enumerate(row):
            
            occ = 0
            dirs = [(0, 0-1), (0, 0+1), (0-1, 0), (0+1, 0),   (0+1, 0+1), (0-1, 0-1), (0+1, 0-1), (0-1, 0+1)]
            for dx, dy in dirs:
                found = False
                incs = 1
                while not found:
                    ax = x + dx * incs
                    ay = y + dy * incs
                    
                    if ax >= 0 and ax <= len(lines[0]) - 1 and ay >= 0 and ay <= len(lines) - 1:
                        aocc = lines[ay][ax]
                        if aocc != ".":
                            found = True
                        if aocc == "#":
                            occ += 1
                    else:
                        found = True
                    
                    incs += 1
            
            if seat == "L" and occ == 0:
                updates += [(x, y, "#")]
            if seat == "#" and occ >= 5:
                updates += [(x, y, "L")]
            
        #    if rounds > 0:
        #        break
        #if rounds > 0:
        #    break

    for x, y, new in updates:
        lines[y][x] = new
    rounds += 1

while True:
    print('\nround')
    before = copy.deepcopy(lines)
    simround()
    after = copy.deepcopy(lines)
    print("\n".join("".join(l) for l in lines))

    if "".join("".join(l) for l in before) == "".join("".join(l) for l in after):
        break

print("____________________-")
print("".join("".join(l) for l in lines).count("#"))


print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
