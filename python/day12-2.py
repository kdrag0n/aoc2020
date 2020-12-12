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
import math

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
while True:
    x = 0
    y = 0
    wx = 10
    wy = 1
    for l in lines:
        print()
        print(l)
        a = l[0]
        v = int(l[1:])
        if a == "N":
            wy += v
        elif a == "S":
            wy -= v
        elif a == "E":
            wx += v
        elif a == "W":
            wx -= v
        elif a == "L":
            rwx, rwy = rotate((0, 0), (wx, wy), math.radians(v))
            wx = int(round(rwx))
            wy = int(round(rwy))
        elif a == "R":
            print('vv', v)
            rwx, rwy = rotate((0, 0), (wx, wy), math.radians(-v))
            wx = int(round(rwx))
            wy = int(round(rwy))
        elif a == "F":
            x += wx * v
            y += wy * v
        else:
            print("BAD ACT")
        print('[w]', wx, wy)
        print('!', x, y)

    print(x, y)
    print(abs(x) + abs(y))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
