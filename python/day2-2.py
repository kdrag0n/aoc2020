#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    lines = [l.split(": ") for l in f.read().split("\n") if l]

valid = 0
for policy, pw in lines:
    crange, letter = policy.split(" ")
    p1, p2 = [int(i) for i in crange.split("-")]

    if len(pw) >= p2:
        p1a = p1 - 1
        p2a = p2 - 1
        if pw[p1a] == letter and pw[p2a] != letter:
            valid += 1
        if pw[p2a] == letter and pw[p1a] != letter:
            valid += 1

print(valid)
