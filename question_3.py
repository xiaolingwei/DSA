# -*- coding: utf-8 -*-
"""
Created on Sun May 23 10:47:17 2021

@author: MYM
"""

import numpy as np
import pandas as pd 
import jieba
import sklearn
from sklearn.feature_extraction.text import CountVectorizer



def get_custom_stopwords(stop_words_file):

    with open(stop_words_file, encoding='utf-8')as f: 
        
        stopwords=f.read()
        stopwords_list=stopwords.split('\n')
        custom_stopwords_list=[i for i in stopwords_list]
    
    return custom_stopwords_list

#加载自定义词语 
jieba.load_userdict("C:/Users/MYM/My_python_codes/DSA/user_dict.txt")

#打开文件，文件在桌面上，可以自行修改路径
f1 = open("C:/Users/MYM/My_python_codes/DSA/text_words.txt","r",encoding='GB2312',errors='ignore')
f2 = open("C:/Users/MYM/My_python_codes/DSA/text_words_token.txt",'w',encoding='GB2312',errors='ignore')
for line in f1:

    seg_list = jieba.cut(line, cut_all = False)
    f2.write((" ".join(seg_list)).replace("\t\t\t","\t"))
    #print(w)
    
f1.close()
f2.close()

# 取需要分词的内容
titles = open("C:/Users/MYM/My_python_codes/DSA/text_words_token.txt", encoding='GB2312', errors='ignore').read().split('\n')
#查看内容，这里是一个list, list里面每个原素是分好的标题，查看下长度看有没有错误



#停用词函数调用
stop_words_file= "C:/Users/MYM/My_python_codes/DSA/CNstopwords.txt"
stopwords = get_custom_stopwords(stop_words_file)



#构建词向量，也就是把分好的次去除停词转化成kmeans可以接受的形式
from sklearn.feature_extraction.text import CountVectorizer

count_vec=CountVectorizer(stop_words = stopwords)
km_matrix= count_vec.fit_transform(titles)
print(km_matrix.shape)

#查看词向量
# print(km_matrix.toarray())

#开始聚类啦
from sklearn.cluster import KMeans

num_clusters = 8 #聚为八类，可根据需要修改
km = KMeans(n_clusters=num_clusters)
km.fit(km_matrix)
clusters = km.labels_.tolist()

#查看聚类的结果，是list,这里省略，看看长度是不是和title一样就行啦
#len(clusters)

#最后把聚类结果写在一个新的txt里面
f3 =open("C:/Users/MYM/My_python_codes/DSA/cluster.txt", 'w',encoding='GB2312',errors='ignore')

for i in clusters:
    f3.write(str(i))
    f3.write("\n")
f3.close()

# f1 = open("C:/Users/MYM/My_python_codes/DSA/text_words.txt","r",encoding='GB2312',errors='ignore')
# f2 = open("C:/Users/MYM/My_python_codes/DSA/text_words_label.txt",'w',encoding='GB2312',errors='ignore')

# counts = 0
# for line in f1:
#     f2.write(str(clusters[counts]))
#     f2.write(' ')
#     counts = counts + 1
#     f2.write(line)
    
# f1.close()
# f2.close()
