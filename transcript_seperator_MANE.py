#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:08:18 2022

@author: chenliu
"""

from nbformat import write


def MANEseperator(file_mane, file_database):
    mane_dic = {}
    with open(file_mane) as fi:
        fi.readline()
        for line in fi:
            li = line.strip().split('\t')
            mane_dic[li[0]] = li[2]
    file_MANE = file_database[:-4] + '.MANE.txt'
    file_MANE_exclude = file_database[:-4] + '.MANE_exclude.txt'
    file_undefined = file_database[:-4] + '.MANE_undefined.txt'

    fo_MANE = open(file_MANE, 'w', encoding='utf-8')
    fo_MANE_ex = open(file_MANE_exclude, 'w', encoding='utf-8')
    fo_undefined = open(file_undefined, 'w', encoding='utf-8')

    with open(file_database, encoding='utf-8') as fi:
        head = fi.readline()
        fo_MANE.write(head)
        fo_MANE_ex.write(head)
        fo_undefined.write(head)
        gene_MANE_li = mane_dic.keys()
        for line in fi:
            li = line.strip().split('\t')
            if li[12] != '-':
                if li[12] in gene_MANE_li:
                    if mane_dic[li[12]] == li[14]:
                        fo_MANE.write(line)
                    else:
                        fo_MANE_ex.write(line)
                else:
                    fo_undefined.write(line)
            else:
                fo_undefined.write(line)
    fo_MANE.close()
    fo_MANE_ex.close()
    fo_undefined.close()

file_mane = '/Users/chenliu/ChenLiu/Learning/Bioinformatics/Web/Project/NGSanalyzerStatic/genome/MANE_GRCh37.txt'
file_database = '/Users/chenliu/ChenLiu/Learning/Bioinformatics/Web/Project/NGSanalyzerStatic/数据库/database_202207.txt'

MANEseperator(file_mane, file_database)