#!/usr/bin/env python

"""
Usage: ./
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


pcafile = pd.read_csv( sys.argv[1], sep= "\t")


        
            
    
plt.figure()
plt.scatter(pcafile["PC1"], pcafile["PC2"], alpha = 0.5, s=1.2)
plt.title("PCA Values")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.savefig( "PCAfile" + ".png")
plt.close()
