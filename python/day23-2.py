#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    cups = ints(f.read().replace("\n", ""))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return f'<{self.value}>'
    def __repr__(self):
        return str(self)


cm = max(cups) + 1
for i in range(1000000 - len(cups)):
    cups.append(cm + i)
cupss = set(cups)
maxc = max(cups)
nodes = [(v, Node(v)) for v in cups]
nlut = dict(nodes)
cups = nodes[0][1]
#link
for i, (_, n) in enumerate(nodes[:-1]):
    n.next = nodes[i+1][1]
last_node = nodes[-1][1]
def llist_to_list(n):
    lst = []
    while n != None:
        lst.append(n.value)
        n = n.next
    return lst
for m in range(10000000):
    if m % 10000 == 0:
        print(f'-- move {m+1} --')
    #print('popl')
    cur = cups.value
    #print('cups:', '  '.join(f'({c})' if c == cur else str(c) for c in llist_to_list(cups)))
    cur_node = cups
    cups = cups.next
    pickup = [cups.value, cups.next.value, cups.next.next.value]
    cups = cups.next.next.next
    #print('pick up:', ', '.join(str(c) for c in pickup))
    destl = cur - 1
    ##print('destsel')
    ###print('    init dest', destl)
    while destl not in cupss or destl in pickup:
        ###print('    cand dest', destl)
        if destl in pickup:
            destl -= 1
        else:
            destl = maxc
    #print('destination:', destl)
    ##print('insert')
    destn = nlut[destl]
    old_next = destn.next
    #print('on', old_next)
    destn.next = nlut[pickup[0]]
    destn.next.next = nlut[pickup[1]]
    destn.next.next.next = nlut[pickup[2]]
    destn.next.next.next.next = old_next
    if old_next == None:
        last_node = destn.next.next.next
    #print('nxts', destn, destn.next, destn.next.next, destn.next.next.next, destn.next.next.next.next)
    ##print('app')
    last_node.next = cur_node
    cur_node.next = None
    last_node = cur_node
    #print('last', last_node, last_node.next)
    #print()

cupl = llist_to_list(cups)
print(cupl[cupl.index(1)+1], cupl[cupl.index(1)+2])
print(cupl[cupl.index(1)+1] * cupl[cupl.index(1)+2])
