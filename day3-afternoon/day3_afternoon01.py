#!/usr/bin/env python

import sys

totalsum = 0
lines = 0

for line in sys.stdin:
    line = line.rstrip()
    totalsum += float(line)
    lines += 1
    
print "the sum is %d, the number of lines is %d, and the average length is %f" % (totalsum, lines, float(totalsum/lines))

    
