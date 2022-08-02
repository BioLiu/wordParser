#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 08:24:58 2022

@author: chenliu
"""

addedfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis/temp/GG.txt"
date_dic = {}
with open(addedfile, encoding="utf-8") as fi:
    for line in fi:
        li = line.split("\t")
        name = li[0].upper()
        if "-" not in name:
            name = name[:3] + "-" + name[3:]
        date_dic[name] = [li[6], li[9]]



dbinput = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis/temp/database_202203edited.txt"
dboutput = dbinput[:-4] + "edited.txt"

with open(dbinput,  encoding="utf-8") as fi:
    with open(dboutput, "w", encoding="utf-8") as fo:
        head = fi.readline()
        fo.write(head)
        for line in fi:
            li = line.split("\t")
            # 字母转为大写
            name = li[0].upper()
            if name in date_dic.keys():
                li[6] = date_dic[name][0]
                li[9] = date_dic[name][1]
            line = "\t".join((li))
            fo.write(line)