"""数据清洗"""
import numpy as np
import pandas as pd

df_1 = pd.read_csv('data_1.csv')
# 用数字0填充空值
print(df_1['salary'].fillna(value=0))
# 用空值的前后一行填充,method可以有不同的值ffill,bfill
print(df_1['salary'].fillna(method='ffill'))
# 使用均值填充
df_1['salary'].fillna(df_1['salary'].mean(), inplace=True)#inplace=True，表示改变了原数据
print(df_1)
# 清除某一列的字符空格
print(df_1['city'][1])#索引是从0开始的
# map()是一个映射操作，对这列的每一个字符串都做同样的操作
df_1['city'] = df_1['city'].map(str.strip)
print(df_1['city'][1])
# 大小写转换
df_1['city'] = df_1['city'].str.lower()
print(df_1)
# 更改数据格式
df_1['id'] = df_1['id'].astype('str')
df_1.info()
df_1['id'] = df_1['id'].astype('int64')
# 更改列名称,inplace=True，直接修改原对象
df_1.rename(columns={'gender': '性别', 'age': '年龄'})

# 删除后出现的值，如只保留第一个本科和高中，后边的都删除
# keep值有'first','last',默认'first':删除重复项，并保留第一次出现的项
# inplace,默认‘False’:是直接在原来数据上进行修改，还是保留一个副本
df_1['education'].drop_duplicates()
# 删除先出现的重复值
df_1['education'].drop_duplicates(keep='last')

# 数据替换
df_1['education'].replace('本科', '大学', inplace=True)
print(df_1)
df_1.to_csv('data_1.csv', index=False)

"""
两种方法改变原数据
1. 方法加入inplace=True参数
2. 新赋值给一个df_1
"""

