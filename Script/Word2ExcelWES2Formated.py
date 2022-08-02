#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:42:14 2022

@author: chenliu

整理文件格式：
1. 样本编号添加-
"""

# 添加
inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/合并/Analysis/2203_CNV.txt"
outputfile = inputfile[:-4]+"_edited.txt"

with open(outputfile, "w", encoding="utf-8") as fo:
    with open(inputfile, encoding="utf-8") as fi:
        head = fi.readline()
        fo.write(head)
        for line in fi:
            li = line.split("\t")
            # 字母转为大写
            li[0] = li[0].upper()
            line = "\t".join((li))
            name = li[0]
            if "-" not in name:
                li[0] = name[:3] + "-" + name[3:]
                line = "\t".join((li))
            fo.write(line)



# 除去重复
def DatabaseSample(dbfile):
    sample_li = []
    with open(dbfile) as fi:
        for line in fi:
            li = line.split("\t")
            sample_li.append(li[0])
    return(sample_li)


def duplicationRemove(inputfile, outputfile, sample_li):
    with open(outputfile, "w", encoding="utf-8") as fo:
        with open(inputfile, encoding="utf-8") as fi:
            for line in fi:
                li = line.split("\t")
                if li[0] not in sample_li:
                    fo.write(line)



databasefile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis/本地数据库_edited.txt"
inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis/2108_2203_edited.txt"
outputfile = inputfile[:-4]+"_added.txt"

sample_li = DatabaseSample(databasefile)

duplicationRemove(inputfile, outputfile, sample_li)



























