#!/usr/bin/env python


"""
counts the number of contigs, minimum/maximum/average contig length, and N50 using my FASTA.py
./dot_plot_script.py <./sorted_velvet_contigs.tsv>
./dot_plot_script.py <./sorted_spades_contigs.tsv>
"""

import sys
import fasta
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools


n50contig = open(sys.argv[1])

count = 1
plt.figure()
for i in n50contig:
    if "#zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count,count+float(fields[1])],[float(fields[0]),float(fields[3])])
        count += float(fields[1])
        
plt.xlabel("Contigs")
plt.ylabel("Contig Position")
plt.ylim((0,100000))
plt.xlim((0,100000))
plt.savefig( "velvet_contigs" + ".png")
plt.close()

        
        



