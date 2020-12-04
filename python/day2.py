#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    lines = [l.split(": ") for l in f.read().split("\n") if l]

valid = 0
for policy, pw in lines:
    crange, letter = policy.split(" ")
    cmin, cmax = [int(i) for i in crange.split("-")]

    ccount = 0
    for char in pw:
        if char == letter:
            ccount += 1

    if ccount >= cmin and ccount <= cmax:
        valid += 1

print(valid)
