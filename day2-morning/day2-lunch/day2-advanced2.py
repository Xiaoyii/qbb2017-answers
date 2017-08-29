#!/usr/bin/env python

import sys

fh = sys.stdin
numlines = 0
twoL = "2L"
begin = 10000
end = 20000



for line in fh:
    if line.startswith("@"):
        continue
    else:
        if (twoL == line.split("\t")[2]):
            if ((line.split('\t')[3]) >= begin) and ((line.split("\t")[3]) <= end):
                numlines +=1
                
            else:
                continue

        
            
print "number: ", numlines