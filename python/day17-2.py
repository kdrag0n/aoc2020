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
MZ = 13
MW = 15

world = copy.deepcopy([[[False] * 10] * 10] * 15)
world = []
for w in range(MW):
    world.append([])
    for z in range(MZ):
        world[w].append([])
        for y in range(MY):
            world[w][z].append([False] * MX)

def pr_wr():
    return
    for w, wlayer in enumerate(world):
        for z, zlayer in enumerate(wlayer):
            print(f"z={z}, w={w}")
            for row in zlayer:
                for ch in row:
                    print("#" if ch else ".", end="")
                print()
            print()

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        world[int(MW//2)][int(MZ//2)][int(MY//2+y)][int(MX//2+x)] = c == "#"
        print(x, y, c, world[int(MZ//2)][y][x], id(world[int(MZ//2)][y]))
print(world[int(MW//2)][int(MZ//2)])
pr_wr()
print("\n\n\n")
while True:
    for cyc in range(6):
        max_z = 1 + cyc * 2
        updates = []

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++ c=", cyc)
        for w in range(MW):
            for z in range(MZ):
                for y in range(MY):
                    for x in range(MX):
                        st = world[w][z][y][x]
                        
                        act_n = 0
                        ncombs = set(itertools.product([1, -1, 0], repeat=4))
                        ncombs -= set([(0, 0, 0, 0)])
                        for dw, dx, dy, dz in ncombs:
                            nw = w + dw
                            nx = x + dx
                            ny = y + dy
                            nz = z + dz
                            if nw >= 0 and nw < MW and nx >= 0 and nx < MX and ny >= 0 and ny < MY and nz >= 0 and nz < MZ:
                                if world[nw][nz][ny][nx]:
                                    act_n += 1
                            else:
                                pass
                                #print('oob -- ', nx, ny, nz)
                        #print(x, y, z, "  act n  ", act_n)
                        
                        if st and not (act_n == 2 or act_n == 3):
                            updates.append((w, x, y, z))
                        elif not st and act_n == 3:
                            updates.append((w, x, y, z))
        
        for w, x, y, z in updates:
            world[w][z][y][x] = not world[w][z][y][x]
        
        pr_wr()
        if (cyc == 2):
            pass
            #exit()

    for wlayer in world:
        for zlayer in wlayer:
            for row in zlayer:
                for ch in row:
                    if ch:
                        total += 1

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
