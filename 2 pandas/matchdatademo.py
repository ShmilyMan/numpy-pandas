# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:43
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : matchdatademo.py
# @Software: PyCharm
import os
import pandas as pd
import numpy  as np
import re

data_directory  = 'D:\\BaiduNetdiskDownload\\data\\matchdata\\201301\\'   # 存放每个月的文件夹的路径
data_files = []  # 存放一个201301目录下文件的列表
files = os.listdir(data_directory)

for f in files:
    data_files.append(f)

# 循环遍历每个文件
dataFormList = []   # 存放df的一个列表
for item in data_files:
    directory = data_directory + item
    # print(directory)
    time = re.search(r'\d+',item).group() # 匹配数字的年份
    df = pd.read_csv(directory)
    df.insert(df.shape[1], 'time', time)    # 新建一个列并插入数据
    dataFormList.append(df)

# 进行文件的合并
data = pd.concat(dataFormList, axis=0, ignore_index=True)
print(data)