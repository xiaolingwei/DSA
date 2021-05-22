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

# 获取特定的列
X = data[['Tag','X1','X2','X3']]
X_ave = get_ave(X, T_num)
X['X_ave'] = X_ave


Sub_dict = dict()

for i in range(1,14):
    Tag = X.loc[X['Tag'] == i]
    Sub_dict.update({'Tag' + str(i):Tag})
    
    
