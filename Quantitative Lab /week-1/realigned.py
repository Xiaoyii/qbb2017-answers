#!/usr/bin/env python

##awk command: less ./blast_alignment.tsv | awk -F '\t' '{ gsub(/-/, ""); print (">" $1 "\n" $2 )}' > 1000_homologs.fa

"""
Reads a peptide sequence and puts the nucleotide sequence from a .fasta file. Puts three -'s for every blank in the peptide
./realigned.py <alignment_prot.fa> <1000_homologs.fa>
"""


import sys
import fasta


peptide = open(sys.argv[1])
nucleotide = open(sys.argv[2])


pep_sequence = []
fasta_identifier = []

for ident, sequences in fasta.FASTAReader( peptide ):
    pep_sequence.append(sequences)
    fasta_identifier.append(ident)
    


nucleotide_sequence = []

for ident, sequences in fasta.FASTAReader( nucleotide ):
    nucleotide_sequence.append(sequences)          


for i in range(len(pep_sequence)):
    codon_pos = 0
    new_seq = "" 
    print ">" + fasta_identifier[i]
    for p in pep_sequence[i]:
        if p == "-":
            new_seq += "---"
        else:
            new_seq += nucleotide_sequence[i][codon_pos:codon_pos+3]
            codon_pos += 3
    print new_seq
    
    
    
# query = []
# target = []
#
# print "hello"
#
# for ident, sequences in fasta.FASTAReader( new_seq ):
#     query.append(sequences[:1:])
#     target.append(sequences[1::])
#
# print "here"
# print query


















