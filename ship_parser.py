#!/usr/bin/env python3

import sys
import os
import pickle


if os.path.exists("ships.p"):
    fin = open("ships.p", "rb")
    ships = pickle.load(fin)
    fin.close()
else:
    ships = {}

for line in sys.stdin.readlines():
    line = line.strip()
    words = line.split()
    if len(words) < 10:
        continue
    x = int(words[1])
    y = int(words[2])
    key = (x,y)
    ships[key] = words
 

fout = open("ships.p", "wb")
pickle.dump(ships, fout)
fout.close()
