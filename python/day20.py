#!/usr/bin/env python3

import sys
from collections import namedtuple
def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n\n") if l]

ilist = []
imap = {}

total = 0
result = 0
other = 0
# 
# 123
# 456
# 789
# 
# 741
# 852
# 963
# 
# 0,0 -> 2,0
# 1,0 -> 2,1
# 2,0 -> 

BorderCandidates = namedtuple('BorderCandidates', ['top', 'bottom', 'left', 'right'])

class Tile():
    def __init__(self, id, view):
        self.id = id
        self.view = view
    def __hash__(self):
        return hash((self.id, tuple(tuple(row) for row in self.view)))

    def hflip(self):
        nv = [list(reversed(row)) for row in self.view]
        return Tile(self.id, nv)

    def vflip(self):
        return Tile(self.id, list(reversed(self.view)))

    def rot(self):
        nv = []
        for i in range(len(self.view)):
            nv.append([" "] * len(self.view[0]))
        for y, row in enumerate(self.view):
            for x, c in enumerate(row):
                nv[x][len(self.view) - 1 - y] = c
        return Tile(self.id, nv)

    def topb(self):
        return tuple(self.view[0])
    def bottomb(self):
        return tuple(self.view[-1])
    def leftb(self):
        return tuple([x[0] for x in self.view])
    def rightb(self):
        return tuple([x[-1] for x in self.view])
    def __str__(self):
        return "\n".join("".join(map(str, x)) for x in self.view)
    def __repr__(self):
        return str(self)
t = Tile(1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(t)
print()
t = t.rot()
print(t)

tiles = []
for l in lines:
    a = [x for x in l.split("\n") if x]
    tid = int(a[0].replace(":", "").replace("Tile ", ""))
    view = [list(x) for x in a[1:]]
    tile = Tile(tid, view)
    tiles += [tile]

    rots = [tile] #, tile.rot(), tile.rot().rot(), tile.rot().rot().rot()]
    for rott in rots:
        tiles += [rott] #, rott.hflip(), rott.vflip()]
tiles = set(tiles)

tile_cands = {}
for mtile in tiles:
    print()
    print()
    print(mtile)
    top_adj = []
    left_adj = []
    right_adj = []
    bottom_adj = []
    for cand in tiles:
        if mtile.topb() == cand.bottomb():
            top_adj += [cand]
        if mtile.bottomb() == cand.topb():
            bottom_adj += [cand]
        if mtile.leftb() == cand.rightb():
            left_adj += [cand]
        if mtile.rightb() == cand.leftb():
            right_adj += [cand]
    print([top_adj, left_adj, right_adj, bottom_adj])
    print()
    tile_cands[mtile] = BorderCandidates(top_adj, bottom_adj, left_adj, right_adj)

# corners
print('\n\n\n\n\n\n')
for mtile, bcands in tile_cands.items():
    if len(bcands.right) == 1 and len(bcands.bottom) == 1 and len(bcands.top) == 0 and len(bcands.left) == 0:
        print(f'top left\n{mtile}', '\n\n\n')


print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
