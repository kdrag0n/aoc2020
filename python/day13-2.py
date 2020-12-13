#!/usr/bin/env python3

import sys
from sympy.ntheory.modular import crt

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
    start = int(lines[0])

    buses = []
    for bus in lines[1].split(","):
        if bus == "x":
            bus = "1"
        bus = int(bus)
        buses.append(bus)

    b1 = []
    b2 = []
    for bi, bus in enumerate(buses):
        print(bi, bus)
        b1.append(bus)
        if bi == 0:
            b2.append(0)
        else:
            b2.append(bus - bi)
    print(b1, b2)

    print(crt(b1, b2))


    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
