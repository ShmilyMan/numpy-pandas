# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 14:24
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 08_pandas plot画图.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 线型的数据
data = pd.Series(np.random.random(1000), index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()

# 字典型的数据
data = pd.DataFrame(np.random.randn(1000,4), columns=['A', 'B', 'C', 'D'])

# data.plot()
# plt.show()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)

plt.show()