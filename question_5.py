# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:31:00 2021

@author: MYM
"""

import numpy as np 
import pandas as pd

# 读取附件2数据
data_get = pd.read_excel('Pro_附件2.xlsx')
#  提取淘汰论文
lose_paper = data_get.loc[data_get['是否淘汰'] == True]
#提取优秀论文
percent = 90
percent_val = np.percentile(data_get['综合得分'], percent)
win_paper = data_get.loc[data_get['综合得分'] > percent_val]


lose_paper = lose_paper[lose_paper['Tag'] == 8]
win_paper = win_paper[win_paper['Tag'] == 8]
lose_paper_val = lose_paper[['选题与综述平均分','创新性及论文价值平均分','科研能力与基础知识平均分','论文规范性平均分','论文总分平均分','综合得分']]
win_paper_val = win_paper[['选题与综述平均分','创新性及论文价值平均分','科研能力与基础知识平均分','论文规范性平均分','论文总分平均分','综合得分']]

lose_mean = lose_paper_val.sum(axis = 0)/len(lose_paper_val)
lose_std = lose_paper_val.std(axis = 0)

win_mean = win_paper_val.sum(axis = 0)/len(win_paper_val)
win_std = win_paper_val.std(axis = 0)



print(lose_paper_val.sum(axis = 0)/len(lose_paper_val))
print(lose_paper_val.std(axis = 0))
print(win_paper_val.sum(axis = 0)/len(win_paper_val))
print(win_paper_val.std(axis = 0))
