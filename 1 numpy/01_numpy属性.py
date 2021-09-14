# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 11:28
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 01_numpy属性.py
# @Software: PyCharm
import numpy as np

array = np.array([[1,2,3],                 # 讲一个二维的列表转换成numpy中的二维数组
                  [3,4,5]])
print(array)
print("数组的形状：",array.shape)         # (2, 3)
print("数组元素的个数：",array.size)      # 6
print("数组的维数：",array.ndim)          # 2