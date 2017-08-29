#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0
MAPQscore = 0


for line in fh:
    if line.startswith("@"):
        continue
    else:
        MAPQscore += int(line.split("\t")[4])
        numlines +=1
        
            
print MAPQscore / numlines