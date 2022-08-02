#!/bin/bash

WorPath="/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/合并/Analysis"
cd ${WorPath}
source /opt/anaconda/anaconda.sh
source activate python34
python ${WorPath}/Word2ExcelWESwithCNV.py -o ${WorPath}/代谢病.txt -d ${WorPath}/代谢病