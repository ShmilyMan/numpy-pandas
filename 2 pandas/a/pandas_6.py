"""数据汇总"""
import numpy as np
import pandas as pd

df_inner = pd.read_csv('data_2.csv')
# 主要函数是 groupby()
# 对所有列进行计数汇总
result = df_inner.groupby('city').count()
print(result)
# 按城市对id字段进行计数
df_inner.groupby('city')['id'].count()
# 对两个字段进行汇总计数
result = df_inner.groupby(['city', 'gender'])['id'].count()
print(result)
# 对city字段进行汇总并分别计算salary的合计和均值
result = df_inner.groupby('city')['salary'].agg([len, np.sum, np.mean])
print(result)

