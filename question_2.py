# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:37:22 2021

@author: MYM
"""

import pandas as pd
import numpy as np


def get_ave(df1, T_num):
    data = df1.values
    ave_data = data.sum(axis = 1) / T_num
    return ave_data



# read xlsx
data = pd.read_excel('附件1.xlsx')
data_get = pd.read_excel('附件2.xlsx')
Num = len(data) # 样本数目
T_num = 3 # the number of teacher

# 获取总分的列
X = data[['Tag','X1','X2','X3']]
X_ave = get_ave(X, T_num)
X['X_ave'] = X_ave


Sub_dict = dict()
for i in range(1,14):
    Tag = X.loc[X['Tag'] == i]
    Sub_dict.update({'Tag' + str(i):Tag})
    
Tag_std_dict = dict()
# 每个学科的三个总分的方差均值，与方差方差
Tag_std_mean = pd.DataFrame(index = ['mean','std'], columns = ['Tag1','Tag2','Tag3','Tag4','Tag5','Tag6','Tag7','Tag8','Tag9','Tag10','Tag11','Tag12','Tag13']) 
for i in range(1,14):
    Tag_val = Sub_dict.get('Tag' + str(i))[['X1','X2','X3']]
    Tag_std = Tag_val.values.std(axis = 1)
    Tag_std_dict.update({'Tag' + str(i):Tag_std})
    Tag_std_mean.loc['mean','Tag'+str(i)] = Tag_std.mean()
    Tag_std_mean.loc['std','Tag'+str(i)] = Tag_std.std()

Tag_std_mean.to_csv('Total scores.csv')

# 计算每个学科的各个项目的得分，与总分平均分水平

# 获取非评语列
Tag_all = data.drop(columns = ['R1','R2','R3'])
Tag_all_dict = dict()
for i in range(1,14):
    Tag_temp = Tag_all.loc[Tag_all['Tag'] == i]
    Tag_all_dict.update({'Tag' + str(i):Tag_temp})
    

Tag_all_mean_dict = dict()

for i in range(1,14):
    Tag_xk1 = Tag_all_dict.get('Tag' + str(i))[['X11','X21','X31']]
    Tag_xk2 = Tag_all_dict.get('Tag' + str(i))[['X12','X22','X32']]
    Tag_xk3 = Tag_all_dict.get('Tag' + str(i))[['X13','X23','X33']]
    Tag_xk4 = Tag_all_dict.get('Tag' + str(i))[['X14','X24','X34']]
    Tag_x = Tag_all_dict.get('Tag' + str(i))[['X1','X2','X3']]
    df1 = pd.DataFrame(index = ['mean','std'], columns = ['Xk1','Xk2','Xk3','Xk4','X'])
    df1['Xk1'] = [Tag_xk1.values.mean(), Tag_xk1.values.std()]
    df1['Xk2'] = [Tag_xk2.values.mean(), Tag_xk2.values.std()]
    df1['Xk3'] = [Tag_xk3.values.mean(), Tag_xk3.values.std()]
    df1['Xk4'] = [Tag_xk4.values.mean(), Tag_xk4.values.std()]
    df1['X'] = [Tag_x.values.mean(), Tag_x.values.std()]
    Tag_all_mean_dict.update({'Tag'+str(i):df1}) # 每个学科的分项与总项的均值与方差（不区分打分老师）
    
    
    
for i in range(1,14):
    if i == 6 or i == 11:
        print('skip')
    else:
        ex = Tag_all_mean_dict.get('Tag' + str(i))
        ex.to_csv('Tag' +str(i)+'.csv')
