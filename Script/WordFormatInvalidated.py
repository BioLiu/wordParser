#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:54:54 2021

@author: chenliu
"""
import os

# inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-已完成-性发育.txt"
# outputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-已完成-性发育-validated.txt"
# fo = open(outputfile, "w")
# with open(inputfile,encoding="utf-8") as fi:
#     invalidated_li = []
#     head = fi.readline()
#     #fo.write(head)
#     for i in fi:
#         li = i.split("\t")
#         omim_info = li[-5]
#         if  "OMIM" in omim_info and "GnomAD" not in omim_info:
#             invalidated_li.append(li[0])
#     invalidated_li = list(set(invalidated_li))

# with open(inputfile,encoding="utf-8") as fi:
#     fi.readline()
#     for line in fi:
#         sample = line.split("\t")[0]
#         if sample not in invalidated_li:
#             fo.write(line)
#     fo.close()

#import os
#file_list = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-骨骼发育-补充-list.txt"
#invalidated_li = []
#with open(file_list) as fi:
#    for line in fi:
#        invalidated_li.append(line.strip())
#invalidated_li = list(set(invalidated_li))
        

# 合并格式错误的文件+格式正确的文件解析结果
file_add = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-已完成-全外显子-补充.txt"
invalidated_li = []
with open(file_add) as fi:
    for line in fi:
        invalidated_li.append(line.split("\t")[0])
invalidated_li = list(set(invalidated_li))

inputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-已完成-全外显子.txt"
outputfile = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/已完成/基因变异本地数据库-已完成-全外显子-validated.txt"
fo = open(outputfile, "w")

with open(inputfile,encoding="utf-8") as fi:
    fi.readline()
    for line in fi:
        sample = line.split("\t")[0]
        if sample not in invalidated_li:
            fo.write(line)
    fo.close()




inputdir = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/备份/全外显子/"
def get_filelist(inputdir): 
    file_dic = {}
    for home, dirs, files in os.walk(inputdir): 
        for filename in files: 
            # 文件名列表，包含完整路径
            if "docx" in filename:
                key = filename.split("_")[0].upper()
                if "-" not in key:
                    key = key[:3] + "-" + key[3:]
                filename_new = filename.replace(" ","_")
                os.rename(os.path.join(home, filename),os.path.join(home, filename_new))
                value = os.path.join(home, filename_new)
                file_dic[key] = value
                # # 文件名列表，只包含文件名     
                # Filelist.append( filename)
            else:
                print(filename) 
    return file_dic

invalidated_dir = "/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/文件格式/"
file_dic = get_filelist(inputdir)
for i in invalidated_li:
    if i in file_dic.keys():
        copycmd = "cp %s %s" %(file_dic[i], invalidated_dir)
        os.system(copycmd)
    else:    
        print(i)


