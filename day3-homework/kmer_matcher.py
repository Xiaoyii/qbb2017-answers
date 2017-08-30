#!/usr/bin/env python

#command: ./kmer_matcher.py subset.fa droYak2_seq.fa 11 | head -n1000
#output file: day3-homework.out

"""
Finds Kmer seeds between target and query

usage: kmer_matcher.py <target.fa> <query.fa> <k>
k is kmer size (integer)
"""

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3]) #will be 11

target_position = {}
query_position = {}


#for target
for ident, sequence in fasta.FASTAReader( target ):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in target_position:
            target_position[kmer] = [(ident, i)]
        else:
            target_position[kmer].append( (ident, i) )

# for kmer, position in target_position.iteritems():
#     print kmer, position


#for query

#can't use for loop, no second ">" to store.
ident, sequence = fasta.FASTAReader( query ).next()

sequence = sequence.upper()
for i in range(0, len(sequence) - k ):
    kmer = sequence[i:i+k]
    if kmer in target_position:
        match = kmer
        for target_name, position in target_position[match]:
            print target_name, "\t", position, "\t", int(i), "\t", kmer

        
        


# for kmer, position in query_position.iteritems():
#     print kmer, position

# target_sequence_name = ident
# target_start = position in target
# query_start = position in query
# kmer = the sequence of the kmer