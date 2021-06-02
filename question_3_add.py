# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:07:12 2021

@author: MYM
"""

import numpy as np 
import pandas as pd


data = pd.read_excel('附件1.xlsx')
# 读取聚类结果
clusters = []
f1 = open("C:/Users/MYM/My_python_codes/DSA/cluster.txt", 'r',encoding='GB2312',errors='ignore')
for line in f1:
    clusters.append(eval(line))

tag_dict = dict()
tag = (1,2,3,4,5,7,8,9,10,12,13)
for i in tag:
    temp = pd.read_csv('Tag'+str(i)+'.csv')
    tag_dict.update({'Tag'+str(i):temp})
num = list()
for i in range(8):
    clusters_temp = [s == i for s in clusters]
    num.append(sum(clusters_temp))

    
right = 0
for i in range(1246):
    Tag = data.loc[i,'Tag']
    mean = tag_dict.get('Tag'+ str(Tag))
    mean_x1 = mean.loc[0,'Xk1']
    mean_x23 = (mean.loc[0,'Xk2'] + mean.loc[0,'Xk3'])/2
    mean_x4 = mean.loc[0,'Xk4']
    s = data.loc[i,'R1'] 
    if pd.isnull(s) or type(s) == int:
        print('nan')
    else:
        if data.loc[i,'X11'] >= mean_x1:
            if (data.loc[i,'X12'] + data.loc[i,'X13'])/2 >= mean_x23 :
                if data.loc[i,'X14'] >= mean_x4:
                    if clusters[i] == 7: # 111 
                        right+=1
                else:
                    if clusters[i] == 6: # 110
                        right+=1
            else:
                if data.loc[i,'X14'] >= mean_x4:
                    if clusters[i] == 5:# 101
                        right+=1
                else:
                    if clusters[i] == 0: # 100
                        right+=1

        else:
            if (data.loc[i,'X12'] + data.loc[i,'X13'])/2 >= mean_x23 :
                if data.loc[i,'X14'] >= mean_x4:
                    if clusters[i] == 4: # 011
                        right+=1

                else:
                    if clusters[i] == 3: # 010
                        right+=1

            else:
                if data.loc[i,'X14'] >= mean_x4:
                    if clusters[i] == 2:# 001
                        right+=1

                else:
                    if clusters[i] == 1: # 000
                        right+=1