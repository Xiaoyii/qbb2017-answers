#!/usr/bin/env python

"""
Usage: ./day5-lunch2.py ~/data/results/stringtie/SRR072893/t_data.ctab 
"""

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


#access the H3K...tab files we made using bigWigAverageOverBed and read them, keep their index numbers
h3k27me3 = pd.read_csv( "H3K27me3.tab", sep = "\t", header=None, index_col=0 )
h3k36me3 = pd.read_csv( "H3K36me3.tab", sep = "\t", header=None, index_col=0 )
h3k4me3 = pd.read_csv( "H3K4me3.tab", sep = "\t", header=None, index_col=0 )
h3k9me3 = pd.read_csv( "H3K9me3.tab", sep = "\t", header=None, index_col=0 )

#access and open the ctab file with FPKM, move the index over to here
df_ctab = pd.read_csv( sys.argv[1], sep = "\t", index_col="t_name" )

#the average is in column 5
h3k27me3_ave = h3k27me3[5]
h3k36me3_ave = h3k36me3[5]
h3k4me3_ave = h3k4me3[5]
h3k9me3_ave = h3k9me3[5]

#concatinate the 4 samples and the FPKMs that we want to compare into one pd file
h3k = pd.concat((h3k27me3_ave, h3k36me3_ave, h3k4me3_ave, h3k9me3_ave, \
df_ctab["FPKM"]), 1, join="inner")

#print h3k

#print "next one"

#calls for statsmodel OLS
model = sm.OLS(h3k["FPKM"], h3k.iloc[:,:4])
results = model.fit()
print (results.summary())





# nsample = 100
# x = np.linspace(0, 10, 100)
# X = np.column_stack((x, x**2))
# beta = np.array([1, 0.1, 10])
# e = np.random.normal(size=nsample)

