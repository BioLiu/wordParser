#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:08:18 2022

@author: chenliu
"""

# 过滤已经解析的报告

def reportFilterAnalyzed(inputfile, outputfile, projectItem, projectLargest):
    # 生成一个应分析列表系列
    sample_list = []
    i = 1
    while i < projectLargest:
        sample = projectItem + str(i)
        sample_list.append(sample)
        i += 1
    
    # 将已经分析的样本放入一个列表
    with open(inputfile, encoding='utf8') as fi:
        sampleAnalyzedlist = []
        for line in fi:
            li = line.strip().split('\t')
            sampleAnalyzedlist.append(li[0])
        sampleAnalyzedlist = list(set(sampleAnalyzedlist))
        
    with open(outputfile, 'w') as fo:
        for item in sample_list:
            if item not in sampleAnalyzedlist:
                fo.write(item + '\n')


inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/合并/Analysis/database_202207.txt"
outputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/合并/database_20220720_QW-B.txt"
projectItem = 'QW-B'
projectLargest = 1400
reportFilterAnalyzed(inputfile, outputfile, projectItem, projectLargest)
            
        
        