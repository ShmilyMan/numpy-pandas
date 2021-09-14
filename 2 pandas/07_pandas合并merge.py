# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 13:28
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 07_pandas合并merge.py
# @Software: PyCharm
import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,on='key'))        # 按照key进行合并
print('--------------合并两个key-----------------')
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
# how = ['left', 'right', 'outer', 'inner']
print(pd.merge(left,right,on=['key1','key2'],how='inner'))  # 相同的才会合并

# indicator  -->   显示合并时的描述信息
print('--------------indicator-----------------')
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(pd.merge(df2,df1,how='outer',on='col1',indicator=True))
print(pd.merge(df2,df1,how='outer',on='col1',indicator='描述'))       # 定义显示时描述的名称

print('--------------index(按照行标进行排序，基本不用)-----------------')
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
print('--------------suffixes:对相同的属性名称定义不同的名字-----------------')
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
