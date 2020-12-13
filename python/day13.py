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

    minid = 1000000000000000000000000
    mint = 10000000000000000000000
    bust = []
    for bus in lines[1].split(","):
        if bus == "x":
            continue
        bus = int(bus)
        minb = int(start / bus) - 1
        for i in range(50):
            t = bus * (minb + i)
            if t <= mint and t >= start:
                minid = bus
                mint = t
        rmn = start % bus
        bust.append((bus, rmn))
        print(f"{start} % {bus} = {rmn}")

    print(min(bust, key=lambda b: b[1]))

    print(minid, mint - start, minid *(mint-start))

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
