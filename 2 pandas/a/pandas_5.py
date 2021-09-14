"""数据筛选"""
import numpy as np
import pandas as pd

df_inner = pd.read_csv('data_2.csv')
# 使用“与”筛选
result = df_inner.loc[((df_inner['city'] == 'beijing') & (df_inner['age'] > 30)), ['age', 'gender']]
print(result)
# 使用“或”筛选: |
# 使用“非”筛选: !=
# 对筛选后的数据按city列进行计数
number = df_inner.loc[df_inner['city'] != 'beijing'].city.count()
print(number)
# 使用query函数进行筛选
df_inner.query("city==['beijing', 'wuhan']")
# 对筛选后的结果进行求和
number = df_inner.query("city==['beijing', 'wuhan']").salary.sum()



