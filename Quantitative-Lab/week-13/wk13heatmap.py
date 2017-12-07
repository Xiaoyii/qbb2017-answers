#!/usr/bin/env python


"""
"""

import sys
import math
import itertools
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hac
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
from sklearn.cluster import KMeans


# a = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0)
# print a

infile = pd.read_csv( sys.argv[1], sep='\t', index_col=0 )[['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]
#save the column/row headers (conditions/genes) into an array

bin_dic = { 'bin.1': 'Staphylococcus haemolyticus', 'bin.2': 'Leuconostoc citreum', 'bin.3': 'Staphylococcus lugdenensis', 'bin.4': 'Enterococcus faecalis', 'bin.5': 'Cutibacterium avidum', 'bin.6': 'Staphylococcus epidermidis','bin.7': 'Staphylococcus aureus', 'bin.8': 'Anaerococcus prevotii' }

genes = []
for bin in infile.index:
    genes.append(bin_dic[ bin ])
    
# print genes
    
plt.figure()
plt.imshow(infile, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Newborn Gut Bacteria ")
plt.colorbar()
plt.xticks( range(len( infile.columns)), infile.columns, rotation = 'vertical')
plt.yticks( [ x for x in range(len(genes)) ], genes)
plt.tight_layout()
plt.savefig("week13_heatmap.png") # Save the image
plt.close()