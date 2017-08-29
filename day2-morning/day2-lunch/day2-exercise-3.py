#!/usr/bin/env python

import sys

fh = sys.stdin
count = 0
perfect_match = "NH:i:1"

for line in fh:
    if perfect_match in line:
        count +=1
    else:
        continue
            
print count
        