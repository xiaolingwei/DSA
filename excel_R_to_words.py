# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:36:06 2021

@author: MYM
"""

import numpy as np
import pandas as pd 

# read xlsx
data = pd.read_excel('附件1.xlsx')

text = open("C:/Users/MYM/My_python_codes/DSA/text_words.txt",'w', encoding='GB2312',errors='ignore')

text_R = data[['R1','R2','R3']]





count = 0 
for s in text_R['R1']:
    if pd.isnull(s) or type(s) == int:
        print('nan')
        count = count + 1 
    else:
        s = s.replace("\n",',')
        text.write(s)
        text.write('\n')
for s in text_R['R1']:
    if pd.isnull(s) or type(s) == int:
        print('nan')
        count = count + 1 
    else:
        s = s.replace("\n",',')
        text.write(s)
        text.write('\n')
for s in text_R['R1']:
    if pd.isnull(s) or type(s) == int:
        print('nan')
        count = count + 1 
    else:
        s = s.replace("\n",',')
        text.write(s)
        text.write('\n')
text.close()



# for i in range(1246):
#     s = text_R.loc[i,'R1']
#     if pd.isnull(s) or type(s) == int:
#         print('nan')
#     else:
#         s = s.replace("\n",',')
#         text.write(s)
#         text.write('\n')
# for i in range(1246):
#     s = text_R.loc[i,'R2']
#     if pd.isnull(s) or type(s) == int:
#         print('nan')
#     else:
#         s = s.replace("\n",',')
#         text.write(s)
#         text.write('\n')
# for i in range(1246):
#     s = text_R.loc[i,'R3']
#     if pd.isnull(s) or type(s) == int:
#         print('nan')
#     else:
#         s = s.replace("\n",',')
#         text.write(s)
#         text.write('\n')
# text.close()