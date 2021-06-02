# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:48:36 2021

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
percent = 5 #  筛选 末尾 5%

# 获取特定的列
X = data[['X1','X2','X3']]
Xk1 = data[['X11','X21','X31']]
Xk2 = data[['X12','X22','X32']]
Xk3 = data[['X13','X23','X33']]
Xk4 = data[['X14','X24','X34']]


X_ave = get_ave(X, T_num)
Xk1_ave = get_ave(Xk1, T_num)
Xk2_ave = get_ave(Xk2, T_num)
Xk3_ave = get_ave(Xk3, T_num)
Xk4_ave = get_ave(Xk4, T_num)

data_get['选题与综述平均分'] = Xk1_ave
data_get['创新性及论文价值平均分'] = Xk2_ave
data_get['科研能力与基础知识平均分'] = Xk3_ave
data_get['论文规范性平均分'] = Xk4_ave
data_get['论文总分平均分'] = X_ave


X['ave'] = X_ave
X['Tag'] = data['Tag']
lose = []
for i in range(1,14):
    if i == 6 or i == 11:
        print('empty')
    else:
        Tag = X.loc[X['Tag'] == i]    
        percent_val = np.percentile(Tag['ave'], percent)
        lose += list(Tag['ave'] < percent_val)


data_get['是否淘汰'] = lose

data_get.to_excel('Pro_附件2.xlsx', index=None)