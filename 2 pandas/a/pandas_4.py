"""数据提取"""
import numpy as np
import pandas as pd

df_inner = pd.read_csv('data_2.csv')
# 主要用到2个函数：loc,iloc
# loc函数按标签值进行提取，iloc按位置进行提取

# 按索引行提取单行的数值
print(df_inner.loc[3])
# 按索引提取区域行数值
print(df_inner.iloc[0:3])
# 提取4日之前的所有数据
print(df_inner.loc[:'2019-10-04'])
# 使用iloc按位置区域提取数据
print(df_inner.iloc[:3, :2])
# 使用iloc按位置单独提取数据
print(df_inner.iloc[[0, 2], [4, 5]])#第0、2行，第4、5个特征（从0开始的）
# 判断city列的值是否为北京
print(df_inner['city'].isin(['beijing']))
# 判断city列里面是否包含beijing和wuhan，然后将符合条件的数据提取出来
result = df_inner.loc[df_inner['city'].isin(['beijing', 'wuhan'])]



