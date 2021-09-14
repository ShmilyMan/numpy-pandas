# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 11:04
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 04_pandas处理丢失的数据.py
# @Software: PyCharm
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(24).reshape((6, 4)), index=pd.date_range('20200112', periods=6),
                     columns=['A', 'B', 'C', 'D'])
frame.iloc[0,1] = np.nan
frame.iloc[1,2] = np.nan

# 1.丢掉缺失数据的行
print(frame.dropna(axis=0,how='any'))   # how='all' --> 当全部为空时才丢掉

# 2.填充缺失的数据
print(frame.fillna(value=0))        # 将缺失的数据填充为0

# 3.判断是否有缺失的数据
print(np.any(frame.isnull()) == True)