#!/usr/bin/env python

##awk command: less ./blast_alignment.tsv | awk -F '\t' '{ gsub(/-/, ""); print (">" $1 "\n" $2 )}' > 1000_homologs.fa

#./realigned.py alignment_prot.fa 1000_homologs.fa > new_seq.fa 


"""
looks for ds and dN changes in the target sequence compared to the query
./target_changes.py <new_seq.fa>
"""

import sys
import fasta
import numpy as np
import matplotlib.pyplot as plt

mapper = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

new_sequence = open(sys.argv[1])


dn = []
ds = []

#4871 from dividing codons by 3
for i in range(0, 4871):
    dn.append(0)
    ds.append(0)
    
nuc_seq = []
for ident, sequences in fasta.FASTAReader( new_sequence ):
    nuc_seq.append(sequences)


query_seq = nuc_seq[:1]
target_seq = nuc_seq[1:]

#print query_seq

# samtools faidx new_seq.fa WNFCG_1

for n in range(len(target_seq)):
    count = 0
    prot_count = 0
    #14614 is the length of every nucelotide
    while count < 14614:
        target = target_seq[n][count:count+3]
        query = query_seq[0][count:count+3]
        if "-" in target_seq[n][count:count+3]:
            count += 3
            prot_count += 1
        elif "-" in query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target_seq[n][count:count+3] == query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target not in mapper:
            count += 3
        elif mapper[target] != mapper[query]:
            dn[prot_count] = dn[prot_count] + 1
            count += 3
            prot_count += 1
        elif mapper[target] == mapper[query]:
            ds[prot_count] = ds[prot_count] + 1
            count += 3
            prot_count += 1
        else:
            print "Error, something was wrong."    
        #print count
# print dn
# print ds

dn_ds = [int(n) - int(s) for n, s in zip (dn, ds)]

mean_dn_ds = np.mean(dn_ds)
std_dev_dn_ds = np.std(dn_ds)
SE_dn_ds = std_dev_dn_ds / np.sqrt(len(dn_ds))
zscore_dn_ds = mean_dn_ds / std_dev_dn_ds

#get the zscore of each individual data point (dn_ds)
new_z = []
for i in dn_ds:
    mean = i - mean_dn_ds
    new_z.append(mean / std_dev_dn_ds)
    
    

non_zero_dn = []
non_zero_ds = []

for i in range(len(dn)):
    non_zero_dn.append(dn[i] + 1)
    non_zero_ds.append(ds[i] + 1)

log_nonzero_dn_ds = [np.log2(float(n)/float(s))for n,s in zip(non_zero_dn, non_zero_ds)]
non_zero_dn_ds = [float(n)/float(s) for n,s in zip(non_zero_dn, non_zero_ds)]

# print non_zero_dn_ds

mean_nonzero = np.mean(non_zero_dn_ds)
std_nonzero = np.std(non_zero_dn_ds)
SE_nonzero = std_nonzero / np.sqrt(len(non_zero_dn_ds))
zscore_nonscore = (mean_nonzero)- 1 / SE_nonzero



print std_dev_dn_ds
print SE_dn_ds
print mean_dn_ds
print zscore_dn_ds
# print "next"
# print mean_nonzero
# print std_nonzero
# print SE_nonzero
# print zscore_nonscore




plt.figure()
plt.scatter( range(len(non_zero_dn_ds)), non_zero_dn_ds, alpha = 0.5 )
plt.title("Normalized dN/dS")
plt.xlabel("Gene Location")
plt.ylabel("dN / dS")
plt.savefig( "scatter_dN_dS" + ".png")
plt.close()


plt.figure()
plt.scatter( range(len(new_z)), new_z, alpha = 0.5 )
plt.title("Individualized Z-Score for each Point")
plt.xlabel("Gene Location")
plt.ylabel("dN / dS")
plt.savefig( "new_indiv_z" + ".png")
plt.close()
    













