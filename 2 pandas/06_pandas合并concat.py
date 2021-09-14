# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 12:55
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 06_pandas合并concat.py
# @Software: PyCharm
import numpy as np
import pandas as pd

data1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
data2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
data3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

# 纵向进行合并
print('------------------1------------------')
data = pd.concat([data1, data2, data3], axis=0, ignore_index=True)
print(data)

print('------------------2------------------')
data4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
data5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd','e'])
'''
    join='outer':合并时没有的列补充为nan
    join='inner':合并时只保留相同的列
'''
data = pd.concat([data5,data4],join='inner')
# print(data)
print('------------------3 apend合并（添加数据）------------------')
data = data1.append([data2, data3], ignore_index=True)      # 添加多个dataframe数据
# 添加单条数据
# series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# data = data1.append(series,ignore_index=True)
print(data)
# print(data)
