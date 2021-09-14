"""数据合并"""
import numpy as np
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', None)
# 保证不换行
pd.set_option('display.width', 1000)

df_1 = pd.read_csv('data_1.csv')
df_2 = pd.DataFrame({'id': [1001, 1002, 1003, 1004, 1005, 1007],
                     'height': [173, 170, 160, 182, 158, 168],
                     'occupation': ['程序猿', '程序猿', '测试', '算法工程师', '程序媛', '程序员鼓励师'],
                     'married': ['Y', 'N', 'N', 'Y', 'Y', 'N']
                     })
# 数据合并：merge\join\concat
# 交集
# on 用于连接的列名，必须存在于左右两个DataFrame对象中
df_inner = pd.merge(df_1, df_2, on='id', how='inner')
print(df_inner)
# 左联接,往df_1上合并,保留df_1有的id,df_2没有的值就填空值
df_left = pd.merge(df_1, df_2, on='id', how='left')
print(df_left)
# 右联接
df_right = pd.merge(df_1, df_2, on='id', how='right')
print(df_right)
# 并集
df_outer = pd.merge(df_1, df_2, on='id', how='outer')

# append方法：新加一条记录
df_3 = pd.DataFrame({'id': [1008],
                     'height': [177],
                     'occupation': ['程序猿'],
                     'married': ['Y']})
result = df_2.append(df_3)
print(result)
print('-------')
print(df_2)

# 设置索引列
# 将id设置为索引
print(df_inner.set_index('id'))
# 按照特定列的值排序
print(df_inner.sort_values(by=['age']))
# 按照索引列排序
print(df_inner.sort_index())

# 添加level列：单个条件
# 如果salary列的值>=6000,level列显示high，否则显示low
# numpy.where(condition, x, y) 满足condition,输出x,否则输出y
df_inner['level'] = np.where(df_inner['salary'] >= 6000, 'high', 'low')
print(df_inner)

# 添加sign列：多个条件
# 对复合多个条件的数据进行分组标记
df_inner.loc[(df_inner['salary'] >= 6000) & (df_inner['gender'] == '男'), 'sign'] = 1
print(df_inner)

# 对like字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名为art和fruit
df_split = pd.DataFrame((x.split('-') for x in df_inner['like']),
                        index=df_inner.index, columns=['art', 'fruit'])#列表嵌套列表
print(df_split)

# 将完成分裂后的数据表和原df_inner数据表进行匹配
df_inner = pd.concat([df_inner, df_split], axis=1)#axis=1表示数据是横着合并的
print(df_inner)
df_inner.to_csv('data_2.csv', index=False)
