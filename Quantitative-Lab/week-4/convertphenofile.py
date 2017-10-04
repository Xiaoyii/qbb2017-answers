#!/usr/bin/env python

"""
Usage: ./convertphenofile.py tabBYxRM_PhenoData.txt
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


phenosplit = []
phenoid = []

pheno = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

for line in pheno:
    if line.startswith("\t"):
        outfile.write("\t" + line + "\n")
        continue
    if line.startswith("A"):
        phenosplit = line.split()
        phenoid = phenosplit[0].replace("_", "\t")
        #print phenoid
        remainder = "\t".join(phenosplit[1:])
        # print remainder
        outfile.write(phenoid + "\t" + remainder + "\n")
        
        

