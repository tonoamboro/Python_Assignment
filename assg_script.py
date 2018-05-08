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
