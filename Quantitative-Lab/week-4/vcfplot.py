#!/usr/bin/env python

"""
Usage: ./vcfplot.py BYxRM_segs_saccer3.bam.simplified.vcf 

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

vcol = []
afnum = []
af = []

vcffile = open( sys.argv[1] )
for line in vcffile:
    if line.startswith ("#"):
        continue
    else:
        line = line.split("\t")
#        print line[7]
        vcfcol = line[7]
        #print vcfcol

    af = vcfcol[3:].split(",")
    # print af
    for i in af:
#        print i
       afnum.append(float(i))

# print afnum




plt.figure()
plt.hist(afnum, bins = 85, facecolor = 'turquoise')
plt.title("Genotype AF")
plt.xlabel("Allele Frequency")
plt.ylabel("Counts")
plt.savefig( "vcfplot" + ".png")
plt.close()
