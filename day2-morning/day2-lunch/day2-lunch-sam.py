#!/usr/bin/env python

import sys

fh = sys.stdin
count = 0

for line in fh:
    if line.startswith("@"):
        continue
    else:
        count += 1
            
print count
        