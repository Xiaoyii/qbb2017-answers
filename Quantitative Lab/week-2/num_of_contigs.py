#!/usr/bin/env python


"""
counts the number of contigs, minimum/maximum/average contig length, and N50 using my FASTA.py
./num_of_contigs.py <./fastqfiles/contigs.fa>
./num_of_contigs.py <./spadesout/contigs.fasta>
./num_of_contigs.py <./MAPsdata/contigs.fasta>
"""

import sys
import fasta
import numpy as np
import matplotlib.pyplot as plt


contigs = open(sys.argv[1])

contig_lens = []
for ident, sequences in fasta.FASTAReader( contigs ):
    contig_lens.append(len( sequences ))
    
    
min_len = min( contig_lens )
max_len = max( contig_lens )
sum_len = sum( contig_lens )
avg_len = sum_len / len( contig_lens )

print "length of contigs: ", len( contig_lens )
print "minimum: ", min_len
print "maximum: ", max_len
print "average contig length: ", avg_len    
    
contig_lens.sort()
i = 0
add_contig = 0
while add_contig < sum( contig_lens ) / 2:
    add_contig += contig_lens[i]
    i += 1

n50 = contig_lens[i]

print "n50: ", n50
    
    




