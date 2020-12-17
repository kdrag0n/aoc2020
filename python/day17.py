#!/usr/bin/env python3

import sys
import itertools
import copy
def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [list(l) for l in f.read().split("\n") if l]
    print(lines)



ilist = []
imap = {}

total = 0
result = 0
other = 0

# zyx
MX = 50
MY = 50
MZ = 50

world = copy.deepcopy([[[False] * 10] * 10] * 15)
world = []
for z in range(MZ):
    world.append([])
    for y in range(MY):
        world[z].append([False] * MX)

def pr_wr():
    for z, layer in enumerate(world):
        print(f"z={z}")
        for row in layer:
            for ch in row:
                print("#" if ch else ".", end="")
            print()
        print()

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        world[int(MZ//2)][int(MY//2+y)][int(MX//2+x)] = c == "#"
        print(x, y, c, world[int(MZ//2)][y][x], id(world[int(MZ//2)][y]))
print(world[int(MZ//2)])
pr_wr()
print("\n\n\n")
while True:

    for cyc in range(6):
        max_z = 1 + cyc * 2
        updates = []

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ c=", cyc)
        for z in range(MZ):
            for y in range(MY):
                for x in range(MX):
                    st = world[z][y][x]
                    
                    act_n = 0
                    ncombs = set(itertools.product([1, -1, 0], repeat=3))
                    ncombs -= set([(0, 0, 0)])
                    for dx, dy, dz in ncombs:
                        nx = x + dx
                        ny = y + dy
                        nz = z + dz
                        if nx >= 0 and nx < MX and ny >= 0 and ny < MY and nz >= 0 and nz < MZ:
                            if world[nz][ny][nx]:
                                act_n += 1
                        else:
                            pass
                            #print('oob -- ', nx, ny, nz)
                    #print(x, y, z, "  act n  ", act_n)
                    
                    if st and not (act_n == 2 or act_n == 3):
                        updates.append((x, y, z))
                    elif not st and act_n == 3:
                        updates.append((x, y, z))
        
        for x, y, z in updates:
            world[z][y][x] = not world[z][y][x]
        
        pr_wr()
        if (cyc == 2):
            pass
            #exit()

    for layer in world:
        for row in layer:
            for ch in row:
                if ch:
                    total += 1

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
