#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0
forward = 0
reverse = 0
mask = 16


for line in fh:
    if line.startswith("@"):
        continue
    else:
        binary = int(line.split("\t")[1])
        if binary & mask:
            reverse +=1
        else:
            forward +=1
        
            
print "number of forward splice reads: ", forward, " and the number of reverse reads: ", reverse