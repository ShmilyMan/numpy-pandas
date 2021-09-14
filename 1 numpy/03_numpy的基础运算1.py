# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 13:51
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 03_numpy的基础运算.py
# @Software: PyCharm
import numpy as np

a = np.array([10,11,12,13])
b = np.arange(4)        # [0,1,2,3]

c = a + b               # 加法
print(c)                # [10 12 14 16]
print('------------------------------')
c = a - b               # 减法
print(c)                # [10 10 10 10]
print('------------------------------')
c = b**2                # 立方
print(c)                # [0 1 4 9]
print('------------------------------')
c = np.sin(a)           # sin,con,tan
print(c)                # [-0.54402111 -0.99999021 -0.53657292  0.42016704]
print('------------------------------')
c = b < 3               # 判断数组中小于三的值有几个，返回一个数组
print(c)                # [ True  True  True False]
print('------------------------------')
a = np.array([[1,2],
              [3,4]])
b = np.arange(4).reshape((2,2))
c = a * b               # 乘法,对应位置上的元素相乘
'''
    [[ 0  2]
    [ 6 12]]
'''
print(c)
c = a.dot(b)            # 矩阵的乘法
'''
    [[ 4  7]
    [ 8 15]]
'''
print(c)
print('------------------------------')
array = np.random.random((2, 3))            # 随机生成0~1之间的矩阵
print(array)
'''
    可以指定axis参数
        0:在列上求
        1:在行上求
'''
print(np.sum(array),np.min(array,axis=1),np.max(array,axis=0))
