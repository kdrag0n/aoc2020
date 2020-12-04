#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n")]



ilist = []
imap = {}

total = 0
result = 0
other = 0

while True:
    fields = {}
    def val():
        print(fields)
        for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if k not in fields:
                return False
        return True
    for l in lines:
        if not l:
            if val():
                total += 1
            fields = {}
            continue
        
        if c.count(":") > 1:
            for tk in l.split(" "):
                print(tk)
                k, v=tk.split(":")
                fields[k]=v
        else:
            k, v=l.split(":")
            fields[k] = v


    if fields:
        if val():
            total += 1
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
