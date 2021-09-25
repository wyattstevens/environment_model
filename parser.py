#!/usr/bin/env python3

import sys
import os
import pickle


if os.path.exists("sectors.p"):
    fin = open("sectors.p", "rb")
    sectors = pickle.load(fin)
    fin.close()
else:
    sectors = {}

for line in sys.stdin.readlines():
    line = line.strip()
    words = line.split()
    if len(words) < 10:
        continue
    x = int(words[1])
    y = int(words[2])
    key = (x,y)
    sectors[key] = words
 

fout = open("sectors.p", "wb")
pickle.dump(sectors, fout)
fout.close()
