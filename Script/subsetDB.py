#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:44:51 2021

@author: chenliu
"""

import argparse

def subsetDB(inputfile, outputfile, diseases):
    dis_li = diseases.split(",")
    with open(outputfile, "w") as fo:
        with open(inputfile) as fi:
            fo.write(fi.readline())
            for line in fi:
                li = line.split("\t")
                dis_info = li[10] + li[11]
                recall   = li[3]
                tag = False
                for i in dis_li:
                    if i in dis_info and recall != "-" and recall != "无":
                        tag = True
                        break
                    else:
                        continue
                if tag:
                    fo.write(line)

parser = argparse.ArgumentParser(description="Subset database with gene.")
parser.add_argument("-i", help="The path of the database.", type=str)
parser.add_argument("-o", help="The path of the output (table file).", type=str)
parser.add_argument("-d", help="Diseases used for search.", type=str)
#parser.add_argument("-g", help="The gene for search.", type=str)
args = parser.parse_args()

if args.i and args.o and args.d:
    inputfile = args.i
    outputfile = args.o
    diseases = args.d
    subsetDB(inputfile, outputfile, diseases)