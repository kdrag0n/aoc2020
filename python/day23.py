#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    cups = ints(f.read().replace("\n", ""))



ilist = []
imap = {}

total = 0
result = 0
other = 0
def idx(l, v):
    try:
        return l.index(v)
    except ValueError:
        return -1
while True:
    for m in range(100):
        print(f'-- move {m+1} --')
        cur = cups[0]
        print('cups:', '  '.join(f'({c})' if c == cur else str(c) for c in cups))
        pickup = cups[1:4]
        print('pick up:', ', '.join(str(c) for c in pickup))
        destl = cups[0] - 1
        print('    init dest', destl)
        while idx(cups, destl) == -1 or destl in pickup:
            print('    cand dest', destl)
            if destl in pickup:
                destl -= 1
            else:
                destl = max(cups)
        print('destination:', destl)
        desti = cups.index(destl)
        cups.insert(desti + 1, pickup[2])
        cups.insert(desti + 1, pickup[1])
        cups.insert(desti + 1, pickup[0])
        cups = cups[4:]
        cups += [cur]
        print()

    print("".join(str(c) for c in [*cups[cups.index(1)+1:], *cups[:cups.index(1)]]))
    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")
