#!/usr/bin/env python

"""
Usage: ./day5-lunch.py ~/data/results/stringtie/SRR072893/t_data.ctab 
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], sep = "\t" )
soi_for = df["strand"] == "+"
soi_bac = df["strand"] == "-"

# print df
# print "modified"

coi = ["chr", "start", "end", "t_name"]


df_forward = pd.DataFrame()
for sample in df[coi][soi_for]:
    df_forward["chr"] = df["chr"][soi_for]
    df_forward["start"] = df["start"][soi_for] - 500
    df_forward["end"] = df["start"][soi_for] + 500
    df_forward["t_name"] = df["t_name"][soi_for]
    
    
df_back = pd.DataFrame()   
for sample in df[coi][soi_bac]:
    df_back["chr"] = df["chr"][soi_bac]
    df_back["start"] = df["end"][soi_bac] - 500
    df_back["end"] = df["end"][soi_bac] + 500
    df_back["t_name"] = df["t_name"][soi_bac]
    
df_together = df_forward.append(df_back)
    
print df_together

positives = df_together["start"] >= 0
df_together = df_together[positives]

df_together.to_csv("day5lunch.bed", "\t", header=False, index=False)   

print "here is everything positive to get my average"
print df_together


# pca = PCA()
#
# df = df.T
#
# fit = pca.fit( df )
#
# x = fit.transform( df )
# #print x.shape
#
#
#
# plt.figure()
# #in numpy must be more explit about the columns to give( the first and second )
# plt.scatter( x[:,0], x[:,1], alpha=0.8, c=sexes )
#
# plt.savefig( sys.argv[2])
# plt.close()
