#!/usr/bin/env python

"""
Usage: ./02-stratify.py <ctab> <prefix>

- goal: visualize how many transcripts are on each chromosome
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a_df = pd.read_csv( sys.argv[1], sep = "\t" )
b_df = pd.read_csv( sys.argv[2], sep = "\t" )

a_log = np.log(a_df["FPKM"] + 1)
b_log = np.log(b_df["FPKM"] + 1)

# print a_log
# print b_log

co_e = np.polyfit(a_log, b_log, 1)
print co_e


fig = plt.figure()
plt.scatter( a_log, b_log, alpha = 0.25, edgecolors = 'none', color = 'royalblue' )

new_a = np.linspace(np.min(a_log), np.max(a_log), 100)
new_b = new_a * co_e[0] + co_e[1] 


plt.plot(new_a, new_b, "paleturquoise")
plt.title("FPKM Values of SRR -893 vs SRR -915")
plt.xlabel( "SRR072893" )
plt.ylabel( "SRR072915" )
plt.xlim(-0.5, 10)
plt.ylim(-0.5, 10)
plt.savefig( sys.argv[3] + ".png" )
plt.close()