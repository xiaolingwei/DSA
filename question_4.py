# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:20:33 2021

@author: MYM
"""

import numpy as np
import pandas as pd


#  每个学科的平均分与标准差
tag_dict = dict()
tag = (1,2,3,4,5,7,8,9,10,12,13)
for i in tag:
    temp = pd.read_csv('Tag' + str(i) + '.csv')
    tag_dict.update({'Tag'+ str(i) : temp})




#  读取聚类结果
clusters = []
f1 = open("C:/Users/MYM/My_python_codes/DSA/cluster_q4.txt", 'r',encoding='GB2312',errors='ignore')
for line in f1:
    clusters.append(eval(line))
    


# 读取附件1
data = pd.read_excel('附件1.xlsx')
all_score = data[['X1','X2','X3']]
count = 0
for i in range(1246):
    Tag = data.loc[i,'Tag']
    mean = tag_dict.get('Tag'+ str(Tag))
    mean_x = mean.loc[0,'X']
    std_x = mean.loc[1,'X']
    s = data.loc[i,'R1'] 
    if pd.isnull(s) or type(s) == int:
        print('nan')
    else:
        if clusters[count] == 0:
            if all_score.loc[i,'X1'] <= mean_x:
                all_score.loc[i,'X1'] = all_score.loc[i,'X1'] + std_x/2
        else:
            if all_score.loc[i,'X1'] >= mean_x:
                all_score.loc[i,'X1'] = all_score.loc[i,'X1'] - std_x/2
for i in range(1246):
    Tag = data.loc[i,'Tag']
    mean = tag_dict.get('Tag'+ str(Tag))
    mean_x = mean.loc[0,'X']
    std_x = mean.loc[1,'X']
    s = data.loc[i,'R2'] 
    if pd.isnull(s) or type(s) == int:
        print('nan')
    else:
        if clusters[count] == 0:
            if all_score.loc[i,'X2'] <= mean_x:
                all_score.loc[i,'X2'] = all_score.loc[i,'X2'] + std_x/2
        else:
            if all_score.loc[i,'X2'] >= mean_x:
                all_score.loc[i,'X2'] = all_score.loc[i,'X2'] - std_x/2
for i in range(1246):
    Tag = data.loc[i,'Tag']
    mean = tag_dict.get('Tag'+ str(Tag))
    mean_x = mean.loc[0,'X']
    std_x = mean.loc[1,'X']
    s = data.loc[i,'R3'] 
    if pd.isnull(s) or type(s) == int:
        print('nan')
    else:
        if clusters[count] == 0:
            if all_score.loc[i,'X3'] <= mean_x:
                all_score.loc[i,'X3'] = all_score.loc[i,'X3'] + std_x/2
        else:
            if all_score.loc[i,'X3'] >= mean_x:
                all_score.loc[i,'X3'] = all_score.loc[i,'X3'] - std_x/2       
f_score = all_score.sum(axis = 1)/3

f_data = pd.read_excel('Pro_附件2.xlsx')
f_data['综合得分'] = f_score
f_data.to_excel('Pro_附件2.xlsx')