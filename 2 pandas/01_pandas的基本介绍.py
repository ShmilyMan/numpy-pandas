# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 13:39
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 01_pandas的基本介绍.py
# @Software: PyCharm
import numpy as np
import pandas as pd

# 1.创建pandas的一个序列
'''
    0     1.0
    1     5.0
    2     7.0
    3     NaN
    4    55.0
    5    66.0
    dtype: float64
'''
s = pd.Series([1,5,7,np.nan,55,66])
# 2.创建pandas的索引
'''
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05', '2021-01-06'],
              dtype='datetime64[ns]', freq='D')
'''
datas = pd.date_range('20210101',periods=6)
# 3.定义dataform
frame = pd.DataFrame(np.random.random((6,4)), index=datas, columns=['a', 'b', 'c', 'd'])# 随机生成数据，分别定义行列
print(frame)
# 4.定义dataform,使用默认的index和columns
data_frame = pd.DataFrame(np.arange(12).reshape(3, 4))
print(data_frame)
# 5.使用字典定义dataform
data_frame = pd.DataFrame({'student':["Li Lei","Han Meimei","Tom"],
                           'score'	:[95,98,92],
                           'gender':['M','F','M']})
print(data_frame)
# 6.获取每个列的类型
print(data_frame.dtypes)
# 7.获取行的名字
print(data_frame.index)     # RangeIndex(start=0, stop=3, step=1)
# 8.获取列的名字
print(data_frame.columns)   # Index(['student', 'score', 'gender'], dtype='object')
# 9.获取其中的值(为numpy的一个二维数组/矩阵)
'''
[['Li Lei' 95 'M']
 ['Han Meimei' 98 'F']
 ['Tom' 92 'M']]
'''
print(data_frame.values)
# 10.描述 (个数，平均值，方差，最小值，最大值)
print(data_frame.describe())
# 11.转置
print(data_frame.T)
# 12.对行或列进行排序
print(data_frame.sort_index(axis=0,ascending=False))    # 对行进行倒序排序
# 13.对值进行排序
print(data_frame.sort_values(by='score'))


