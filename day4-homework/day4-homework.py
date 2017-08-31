#!/usr/bin/env python

"""
Usage: ./day4-homework.py <samples.csv> <ctab_dir> <replicates.csv>

- plot timecourse of FBtr0331261 for females and males
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

#DataFrame for females, males, and their replicates
df_samples = pd.read_csv( sys.argv[1] )
df_samples_rep = pd.read_csv( sys.argv[3])

#sample of interest for each
soi_f = df_samples["sex"] == "female"
soi_m = df_samples["sex"] == "male"
soi_fr = df_samples_rep["sex"] == "female"
soi_mr = df_samples_rep["sex"] == "male"

#set up empty lists for fpkms
fpkms_f = []
fpkms_m = []
fpkms_fr = []
fpkms_mr = []



#for females
for sample in df_samples["sample"][soi_f]:
    #build complete file path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" ) #os.path just concatinates the [fields]
    #read current sample
    df = pd.read_csv(fname, sep = "\t")
    # subset just Sxl rows
    roi1 = df["t_name"] == transcript
    #save FPKM values to list
    fpkms_f.append( df[roi1]["FPKM"].values )


#for males
for sample in df_samples["sample"][soi_m]:
    #build complete file path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" ) #os.path just concatinates the [fields]
    #read current sample
    df = pd.read_csv(fname, sep = "\t")
    # subset just Sxl rows
    roi2 = df["t_name"] == transcript
    #save FPKM values to list
    fpkms_m.append( df[roi2]["FPKM"].values )


#for female replicates
for sample in df_samples_rep["sample"][soi_fr]:
    #build complete file path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" ) #os.path just concatinates the [fields]
    #read current sample
    df = pd.read_csv(fname, sep = "\t")
    # subset just Sxl rows
    roi1 = df["t_name"] == transcript
    #save FPKM values to list
    fpkms_fr.append( df[roi1]["FPKM"].values[0] )


#for male replicates
for sample in df_samples_rep["sample"][soi_mr]:
    #build complete file path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" ) #os.path just concatinates the [fields]
    #read current sample
    df = pd.read_csv(fname, sep = "\t")
    # subset just Sxl rows
    roi2 = df["t_name"] == transcript
    #save FPKM values to list
    fpkms_mr.append( df[roi2]["FPKM"].values[0] )


print fpkms_f, fpkms_m, fpkms_fr, fpkms_mr

plt.figure()
plt.plot(fpkms_f, "r", label = "females")
plt.plot(fpkms_m, "b", label = "males")
plt.plot([4, 5, 6, 7], fpkms_fr, "ro", label = "female replicates")
plt.plot([4, 5, 6, 7], fpkms_mr, "bo", label = "male replicates")
plt.title("$\it{Sxl}$", fontsize=25)
plt.xlabel( "Developmental Stage" )
plt.ylabel( "mRNA Abundance (RPKM)" )
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], [ "10", "11", "12", "13", "14A", "14B", "14C", "14D"])

#legend for my plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

# way to adjust size of graph
# plt.subplots_adjust(left=0.1, right=0.65, top=0.9, bottom=0.1)

#way to adjust size of whole png
plt.savefig( "fandm.png", bbox_inches="tight" )
plt.close()










