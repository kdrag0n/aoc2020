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
            x = int(fields.get("byr", "0"))
            if not (x >= 1920 and x <= 2002):
                return False
            x = int(fields.get("iyr", "0"))
            if not (x >= 2010 and x <= 2020):
                return False
            x = int(fields.get("eyr", "0"))
            if not (x >= 2020 and x <= 2030):
                return False
            x = fields.get("hgt", "0asxc")
            if x.endswith("cm"):
                y= int(x.replace("cm","")) 
                if not (y >= 150 and y <= 193):
                    return False
            elif x.endswith("in"):
                y= int(x.replace("in","")) 
                if not (y >= 59 and y <= 76):
                    return False
            else:
                return False
            x = fields.get("ecl", "dasdd")
            if x not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            x = fields.get("hcl", "ASD")
            if not x.startswith("#"):
                return False
            if len(x) != 7:
                return False
            try:
                int(x[1:], 16)
            except ValueError:
                return False
            x = fields.get("pid", "SAD")
            if len(x) != 9:
                return False
            try:
                int(x)
            except ValueError:
                return False
        return True
    for l in lines:
        if not l:
            if val():
                total += 1
            print('clrclrclrclrclrclrclrclrclr')
            fields = {}
            continue
        
        print(l)
        if sum(1 for c in l if c==":") > 1:
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
