# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 19:00
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 02_pandas选择数据.py
# @Software: PyCharm
import numpy as np
import pandas as pd

datas = pd.date_range('20200112',periods=6)
frame = pd.DataFrame(np.arange(24).reshape((6, 4)), index=datas, columns=['A', 'B', 'C', 'D'])
print(frame)
# 1.选择列的数据
print('-------------------')
print(frame['A'])
print(frame.A)
# 2.选择行的数据
print('-------------------')
print(frame[0:3])
print(frame['20200112':'20200113'])
# 3.通过标签进行选择
print('-------------------')
print(frame.loc['20200112'])        # 更具体一点
print('-------------------')
print(frame.loc['20200112',['A','B']])
# 4.通过索引进行选择
print('-------------------')
print(frame.iloc[1:3,1:4])          # 筛选1到3行，1到4列
print(frame.iloc[[1,3,5],1:4])      # 筛选1,3,5行，1到4列
# 5.bool类型的筛选
print('-------------------')
print(frame[frame.A>8])