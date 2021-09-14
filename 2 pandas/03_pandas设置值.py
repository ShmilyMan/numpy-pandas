# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 10:27
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 03_pandas设置值.py
# @Software: PyCharm
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(24).reshape((6, 4)), index=pd.date_range('20200112', periods=6),
                     columns=['A', 'B', 'C', 'D'])
# 1.对DataFrame设置值
# frame.iloc[2,2] = 222
frame.loc['20200112','A'] = 333
frame.A[frame.A > 5] = 0    # 将A列中所有大于五的值都修改成0
print(frame)

# 2.添加新的一列
frame['E'] = np.nan
# frame['F'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20200112', periods=6))
frame['F'] = [1,2,3,4,5,6]
print(frame)

