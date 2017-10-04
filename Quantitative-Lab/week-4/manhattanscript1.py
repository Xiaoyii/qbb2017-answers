#!/usr/bin/env python

"""./manhattanscript1.py <plink.P10.assoc.linear (or another file)>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pvalue = []
pnums = []
pvas = []
good_x = []
good_y = []
bad_x = []
bad_y = []

pfiles = open( sys.argv[1] )
count = 0
for line in pfiles:
    if line.startswith(" ") or "NA" in line:
        continue
    else:
        cutoff = -np.log( 0.00005 )
        line = line.rstrip("\r\n").split()
        count += 1
        # print count
        pvalue = -np.log( float(line[8]) )
        # print pvalue
        if pvalue > cutoff:
            good_x.append( count )
            good_y.append( pvalue )
        else: 
            bad_x.append( count )
            bad_y.append( pvalue )
# print good_x
# print bad_x

# print pvas

plt.figure()
plt.scatter( good_x, good_y, color = 'turquoise', alpha = 0.5 )
plt.scatter( bad_x, bad_y, color = 'crimson', alpha = 0.5 )
plt.title("Manhattan Plot" + sys.argv[1])
plt.ylabel("-log(P-Value)")
plt.xlabel("SNP")
plt.savefig( "Manhan" + sys.argv[1] + ".png")
plt.close()
