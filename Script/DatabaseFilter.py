#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:51:49 2022

@author: chenliu
"""
##  提取特定科室数据

def reportsFilter(inputfile, department):
    outputfile = inputfile[:-4]+"_" + department + ".txt"
    with open(outputfile, "w", encoding="utf-8") as fo:
        with open(inputfile, encoding="utf-8") as fi:
            head = fi.readline()
            fo.write(head)
            for line in fi:
                li = line.split("\t")
                if department in li[7]:
                    fo.write(line)


inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis/database_202203.txt"
department = "遗传"
reportsFilter(inputfile, department)