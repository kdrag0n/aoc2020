#!/usr/bin/env python3

import sys

import re

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

rules2 = {}
rules = {}

def add_rules2(col, dest):
    print(col, '->', dest)
    if dest not in rules2:
        rules2[dest] = {}
    for qty, subcol in rules[col]:
        rules2[dest][subcol] = qty
        add_rules2(subcol, dest)

def search_rules2(col):
    total = 0
    for rootcol, crs in rules2.items():
        for ccol, qty in crs.items():
            print(rootcol, ':', ccol)
            if ccol == col:
                print('+')
                total += 1
    return total

while True:
    for l in lines:
        #grps = re.match(r"^(.+) bags contain (\d+ (.+) bags,?\s*)+.")
        srccol, b = l.split(" bags contain ")
        if srccol not in rules:
            rules[srccol] = []
        for x in b.split(", "):
            if "no o" not in x:
                z = x.replace(" bags", "").replace(" bag", "").replace(".", "")
                qty, subcol = z.split(" ", 1)
                rules[srccol] += [(int(qty), subcol)]
                added = True
                print(srccol, qty, subcol)
    for srccol, crs in rules.items():
        add_rules2(srccol, srccol)


    sc = "shiny gold"
    total = search_rules2(sc)
    print(total)

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
