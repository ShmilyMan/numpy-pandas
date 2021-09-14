"""查看数据信息"""
import numpy as np
import pandas as pd

# 创建数据表,DataFrame类
df = pd.DataFrame({'id': [1001, 1002, 1003, 1004, 1005, 1006],
                   'birth': pd.date_range(start='20191001', periods=6, freq='D'),
                   'city': ['beijing', ' wuhan', 'shangHai', 'beijing', 'Shanghai', 'BEIJING'],
                   'age': [33, 27, 35, 27, 42, 23],
                   'gender': ['男', '男', '女', '男', '女', '女'],
                   'education': ['本科', '高中', '本科', '本科', '高中', '本科'],
                   'salary': [6000, 4000, 5000, 7000, np.nan, 3500],
                   'like': ['sing-apple', 'dance-banana', 'sing-orange',
                            'draw-apple', 'dance-orange', 'sing-orange']
                   })
df.to_csv('data_1.csv', index=False)#index默认为True,是否保留行索引
# 读取CSV文件
df_1 = pd.read_csv('data_1.csv')
print(df_1)

# 1.查看表有几行、几列
print(df_1.shape)
# 2.查看数据基本信息(维度、列名称、数据格式、所占空间）
df_1.info()
# isnull().sum():得到每列缺失值的数量
print(df_1.isnull().sum().sort_values(ascending=False))#False为降序，True为升序
# 3.每一列数据的格式
print(df_1.dtypes)
# 4.某一列格式
print(df_1['id'].dtype)
# 5.空值
print(df_1.isnull())#如果数值为空，就显示True
# 6.查看某一列空值
print(df_1['salary'].isnull)
# 7.查看某一列的唯一值
print(df_1['gender'].unique())
# 8.查看某一列有多少类不同值，并计算每类不同值在该列有多少重复值，查看有多少个男生，女生
print(df_1['gender'].value_counts(dropna=False))#dropna=False就打印出空值的个数
# 9.查看数据表的值(不要表头和index)
print(df_1.values)
# 10.查看列名称
print(df_1.columns)
# 11.查看前n行，后n行数据
print(df_1.head(4))
print(df_1.tail())#默认查看5行数据
"""
sort_values():进行排序
value_counts():查看列表某列有多少个城市，每个城市有多少个人
"""





