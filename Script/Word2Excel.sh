#!/bin/bash

WorPath="/Users/chenliu/ChenLiu/Learning/Bioinformatics/python-docx/2108_2203/Analysis"
cd ${WorPath}
source /opt/anaconda/anaconda.sh
source activate python34
python ${WorPath}/Word2ExcelWES.py -o ${WorPath}/单独添加.txt -d ${WorPath}/单独添加