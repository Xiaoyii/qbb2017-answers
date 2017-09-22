#!/usr/bin/env python

"""
Usage: ./vcfplot.py
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

vcol = []
afnum = []

vcffile = open( sys.argv[1] )
for line in vcffile:
    if line.startswith ("#"):
        continue
    else:
        line = line.split()
        vcfcol = line[7].split(";")
        
    af = vcfcol[3][3:]
    if "," in af:
        af = af.split(",")
        for i in af:
            afnum.append(float(i))
    else:
        afnum.append(float(af))
        
# print afnum
        
        
            
    
plt.figure()
plt.hist(afnum, bins = 20, facecolor = 'turquoise')
plt.title("Filtered AF")
plt.xlabel("Allele Frequency")
plt.ylabel("Counts")
plt.savefig( "vcfplot" + ".png")
plt.close()
