"""数据统计"""
import numpy as np
import pandas as pd

df_inner = pd.read_csv('data_2.csv')
# 简单的数据采样
result = df_inner.sample(n=3)
print(result)
# 手动设置采样权重
weights = [0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights)
# 采样后不放回
df_inner.sample(n=3, replace=False)
# 采样后放回
result = df_inner.sample(n=4, replace=True)
print(result)
# 数据表描述性统计!!!!!
result = df_inner.describe().round(2).T
print(result)
# 计算列的标准差
df_inner['salary'].std()
# 计算两个字段间的协方差
df_inner['salary'].cov(df_inner['age'])
# 计算数据表中所有字段的协方差
df_inner.cov()
# 计算两个字段的相关性分析
df_inner['salary'].corr(df_inner['age'])
# 数据表的相关性分析
result = df_inner.corr()
print(result)

