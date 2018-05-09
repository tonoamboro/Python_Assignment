#!/usr/bin/env python3

import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt

#This function is for tracing false alphabets in the DNA sequence
def false_alphabet(seq):
    f_alphabets = {}
    for al in seq:
        if al not in 'GCAT':
            if al in f_alphabets: f_alphabets[ al ] += 1
            else: f_alphabets[ al ] = 1
    if f_alphabets != {}:
        return f_alphabets

#This function is the method to count kmers
def count_kmers(seq, k):
    counts = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
    return counts

#This function is the method to generate table in .csv file
def generate_table(data_contents, dna_name):
    content = pd.DataFrame([[c[0], c[1], c[2]] for c in data_contents],
    columns=['k', 'observed kmers', 'possible kmers'])
    content.to_csv('output/tables/'+dna_name+'.csv', index=False)

#This line is the main function to call the functions listed in the above
if __name__ == "__main__":
    filename=sys.argv[1]
    if filename in glob.glob('*.fasta'):
        f = open(filename,'r')
        seq = f.readlines()
        dna_name_list = []
        observed_total_counts = []
        possible_total_counts = []
        linguistic_complexity_counts = []

        for line_num, line in enumerate(seq[0:len(seq)]):
            if len(line) > 1 :
                if '>' in line :
                    #print("Species Name", line)
                    line = line.replace(">", "")
                    dna_name = line.rstrip()
                    dna_name_list.append(dna_name)
                else:
                    seq = line.rstrip()
                    #print("DNA Sequence =", seq)
                    f_alphabets = false_alphabet(seq)
                    if f_alphabets != None:
                        print()
                        print('you may check this sequence', line)
                        print('failed to generate output for the sequnce/s in the above due to false alphabet/s', f_alphabets)
                        print()
                        #exit()
                    else:
                        k_counts = []
                        observed_counts = []
                        possible_counts = []

                        for k in range(1,len(seq)+1):
                            if k == 1:
                                possible = 4
                            else:
                                possible = len(seq) - k + 1
                            counts = count_kmers(seq, k)
                            observed = len(counts)
                            k_counts.append(k)
                            observed_counts.append(observed)
                            possible_counts.append(possible)
                            #print(k_list, observed_list, possible_list)

                        #counts the total observed and possible kmers
                        observed_total = sum(observed_counts)
                        possible_total = sum(possible_counts)
                        linguistic_complexity = observed_total/possible_total
                        observed_counts.append(observed_total)
                        observed_total_counts.append(observed_total)
                        possible_counts.append(possible_total)
                        possible_total_counts.append(possible_total)
                        linguistic_complexity_counts.append(linguistic_complexity)
                        k_counts.append('Total');

                        #put the data into the table
                        data_contents = list(zip(k_counts, observed_counts, possible_counts))
                        contents = generate_table(data_contents, dna_name)
                        #print(list(merge_counts))

    else:
        print('file is not recognized')
