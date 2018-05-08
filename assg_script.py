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

#This line is the main function to call all the functions in the above
if __name__ == "__main__":
    filename=sys.argv[1]
    if filename in glob.glob('*.fasta'):
        f = open(filename,'r')
        seq = f.readlines()

        for line_num, line in enumerate(seq[0:len(seq)]):
            if len(line) > 1 :
                if '>' in line :
                    print("Species Name", line)
                else:
                    seq = line.rstrip()
                    print("DNA Sequence =", seq)
                    f_alphabets = false_alphabet(seq)
                    if f_alphabets != None:
                        print('fail to execute DNA sequence due to false alphabet', f_alphabets)
                        exit()
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

                    observed_total = sum(observed_counts)
                    possible_total = sum(possible_counts)
                    linguistic_complexity = observed_total/possible_total
                    observed_counts.append(observed_total)
                    possible_counts.append(possible_total)
                    k_counts.append(linguistic_complexity)
                    merge_counts = zip(k_counts, observed_counts, possible_counts)
                    print(list(merge_counts))
    else:
        print('file is not recognized')
