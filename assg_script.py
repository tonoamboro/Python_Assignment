#!/usr/bin/env python3

import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np

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

#This function is the method to generate graph for linguistic complexity
def generate_lc_graph(filename, dna_name_list, linguistic_complexity_counts):
    objects = dna_name_list
    y_pos = np.arange(len(objects))
    value = linguistic_complexity_counts
    plt.bar(y_pos, value, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value')
    plt.xlabel('Species')
    plt.title('Linguistic Complexity')
    graph_name = filename + 'lc.png'
    plt.savefig('output/graphs/'+graph_name)

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
                        print('Process stopped! Failed to generate outputs due to false alphabet/s', f_alphabets)
                        print('You should correct this sequence before you proceed any further!', line)
                        print()
                        exit()
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

                        #generate the data into the table
                        data_contents = list(zip(k_counts, observed_counts, possible_counts))
                        contents = generate_table(data_contents, dna_name)
                        #print(list(merge_counts))

                        #generate lingustic complexity graph
                        lc_graph = generate_lc_graph(filename, dna_name_list, linguistic_complexity_counts)

    else:
        print('file is not recognized')
