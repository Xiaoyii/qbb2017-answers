#!/usr/bin/env python

"""./wk13kraken.py 
"""

import sys
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import math
# import itertools
# import os

a = open(sys.argv[1])

# print a

kronadict = {}

for line in a:
    item = line.strip('\n').split('\t')
    if item[1] not in kronadict:
        kronadict[item[1]] = 1
    else:
        kronadict[item[1]] += 1
        
for a in kronadict:
    print str(kronadict[a]) + "\t" + "\t".join(a.split(";"))
    
# print kronadict

       










