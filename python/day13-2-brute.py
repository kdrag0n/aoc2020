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
    start = int(lines[0])

    buses = []
    for bus in lines[1].split(","):
        if bus == "x":
            bus = "1"
        bus = int(bus)
        buses.append(bus)
    for t in range(1000000000000000000000000):
        if t % 5000 == 0:
            print(t)
        bval = False
        for bi, bus in enumerate(buses):
            bval = (t+bi) % bus == 0
            if not bval:
                break
        if  bval:
            break
    print(t)
    minid = 1000000000000000000000000
    mint = 10000000000000000000000


    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
