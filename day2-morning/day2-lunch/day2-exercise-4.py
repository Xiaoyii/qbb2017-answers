#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0


for line in fh:
    if line.startswith("@"):
        continue
    else:
        if numlines < 10:
            numlines +=1
            print line.split("\t")[2]
                
            
       
    
            
print numlines
        