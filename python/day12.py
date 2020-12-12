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
    x = 0
    y = 0
    rot = 90
    for l in lines:
        a = l[0]
        v = int(l[1:])
        if a == "N":
            y += v
        elif a == "S":
            y -= v
        elif a == "E":
            x += v
        elif a == "W":
            x -= v
        elif a == "L":
            rot -= v
        elif a == "R":
            rot += v
        elif a == "F":
            if rot == 0:
                y += v
            elif rot == 90:
                x += v
            elif rot == 180:
                y -= v
            elif rot == 270:
                x -= v
            else:
                print("BAD ROT", rot)
        else:
            print("BAD ACT")
        rot = rot % 360
        print('rot', rot)

    print(x, y)
    print(abs(x) + abs(y))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
