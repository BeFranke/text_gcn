#!/usr/bin/python
#-*-coding:utf-8-*-

import pandas as pd

dataset_name = 'amazon'
df_train = pd.read_csv("data/amazon/train.csv")
df_test = pd.read_csv("data/amazon/test.csv")


sentences = list(df_train["Text"]) + list(df_test["Text"])
labels = list(df_train)
train_or_test_list = ['train', 'test']


meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)

f = open('data/corpus/' + dataset_name + '.txt', 'w')
f.write(corpus_str)
f.close()