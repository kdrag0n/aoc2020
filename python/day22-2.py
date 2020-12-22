#!/usr/bin/env python3

import sys
import collections

def ints(itr):
    return [int(i) for i in itr if i]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0
games = 0
def cscore(cs):
    sc = 0
    for i, c in enumerate(reversed(cs)):
        sc += c * (i+1)
    return sc
def play(p1c, p2c):
    global total
    global games
    games += 1
    if games % 1000 == 0:
        print('play', games)
    #print('PLAY', p1c, p2c)
    p1w = False

    hist = set()

    while p1c and p2c:
        hentry = (tuple(p1c), tuple(p2c))
        if hentry in hist:
            p1w = True
            break
        c1 = p1c.pop(0)
        c2 = p2c.pop(0)

        if len(p1c) >= c1 and len(p2c) >= c2:
            p1win = play(p1c[:c1].copy(), p2c[:c2].copy()) == 1
        else:
            p1win = c1 > c2
        if p1win:
            p1c += [c1, c2]
        else:
            p2c += [c2, c1]
        hist.add(hentry)
    if p1win or p1c:
        total = cscore(p1c)
        return 1
    elif p2c:
        total = cscore(p2c)
        return 2

while True:
    p1c = ints(lines[0].split("\n")[1:])
    p2c = ints(lines[1].split("\n")[1:])
    play(p1c, p2c)
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
