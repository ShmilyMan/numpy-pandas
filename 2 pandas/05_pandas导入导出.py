# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 11:14
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 05_pandas导入导出.py
# @Software: PyCharm
import pandas as pd

# 数据的导入
data = pd.read_csv('genome-tags.csv')
print(data)

# 数据的导出
# data.to_csv('a.csv',index=False)    # 不存取行的索引  header = False 不存储列索引
data.to_json('a.json',orient='index')