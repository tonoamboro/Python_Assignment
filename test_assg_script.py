#!/usr/bin/env python3

from assg_script import count_kmers
import pytest

@pytest.fixture
def seq():
    seq = 'TTATTAATGAACCCCTAC'
    return seq

#test k = 2 produces 9 Kmers
def test_counts_kmers2(seq):
    counts = count_kmers(seq, 2)
    assert len(counts) == 9

#test k = 4 produces 15 kmers
def test_counts_kmers4(seq):
    counts = count_kmers(seq, 4)
    assert len(counts) == 15

#test k = 19 (more than seqence) produces 0 kmers
def test_counts_kmers19(seq):
    counts = count_kmers(seq, 19)
    assert len(counts) == 0
