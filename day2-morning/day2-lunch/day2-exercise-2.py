#!/usr/bin/env python

import sys

fh = sys.stdin
count = 0
perfect_match = "MD:Z:40"

for line in fh:
    if perfect_match in line:
        count +=1
    else:
        continue
            
print count
        