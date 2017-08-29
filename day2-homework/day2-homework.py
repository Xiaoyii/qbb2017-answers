#!/usr/bin/env python


import sys

drome = "DROME"
gene_names_counts = {}

for line in sys.stdin:  
    fields = line.rstrip("\r\n").split()
    
    if drome in line:
        if len(fields) == 4:
            fly_base_id = fields[3]
            uniprot_id = fields[2]
            print fly_base_id, "\t", uniprot_id
        else:
            continue

  


