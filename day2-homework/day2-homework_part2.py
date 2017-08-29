#!/usr/bin/env python

#command: ./day2-homework_part2.py homework_part1_map.txt ~/data/results/stringtie/SRR072893/t_data.ctab 


import sys

#mapped_results is named homework_part1_map.txt
mapped_results = open(sys.argv[1])

#ctab_file is named ~/data/results/stringtie/SRR072893/t_data.ctab
ctab_file = open(sys.argv[2])

#create dictionary
mapped_results_dict = {}

#make my part 1 into a dictionary
for line in mapped_results:  
    fields = line.rstrip("\r\n").split("\t")
    #                   FlyID        Uniprot ID            
    mapped_results_dict[fields[0].rstrip(" ")] = fields[1]

#uniprox values into ctab or N/A if no match
#stop after line 100
i = 0
for line in ctab_file:
    i += 1
    if i < 101:
        ctab_fields = line.rstrip("\r\n").split("\t")
        key = ctab_fields[8]
        if key in mapped_results_dict:
            print line, mapped_results_dict[key]
        
        else:
            print line, " N/A"
            
    else:
        break
        

        
    