#!/usr/bin/env python3
# -*- coding: utf-8 -*-

seq = """ >chr21
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCGTGCAGTCAGTG
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TTGTGACTGAAGGGCATGTGTTCAGGCAAGATTGTTGGGTGGCTGTGTTT
TGTCTTCTTCCAGCTCGGCCATGGAATAGCCTGTGGGGACCTACTCTGTG
GTCCCCAGGGAGCTACTCTGTGGGGGCTGTTTCTGTTCAGCAGGGAAGGC
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TCACAGATGACAGTTACTTCCCTAGGTAGTCTGCATGTTGGGCCTCCCAG"""

counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}

for base in seq:
    if base == 'A':
        counts['A'] += 1

print(counts)