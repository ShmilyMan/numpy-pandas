# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 13:29
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 02_numpy创建数组（矩阵）.py
# @Software: PyCharm
import numpy as np

# 1、创建一个二维的数组并定义数组中数字的类型
array = np.array([[1,2,3],
                  [4,5,6]],dtype=int)
print(array.dtype)                          # int32

# 以下默认基本都为float类型
# 2、创建全部元素都为1的数组
array = np.ones((2,3))
print(array)                        # [[1. 1. 1.]   [1. 1. 1.]]

# 3、创建全部元素都为0的数组
array = np.zeros((2,3))
print(array)                        # [[0. 0. 0.] [0. 0. 0.]]

# 4、生成空的数组（矩阵）
array = np.empty((2,3),dtype=float)
print(array)                        # [[0. 0. 0.] [0. 0. 0.]]

# 5、生成数字连续的数组（矩阵）
'''
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
'''
array = np.arange(12).reshape((3, 4))
print(array)

# 5、生成0-10的线段（连续的）
'''
    [[ 0.  2.  4.]
    [ 6.  8. 10.]]
'''
array = np.linspace(0, 10, 6).reshape((2, 3))
print(array)

# 6、随机生成0~1之间的矩阵
array = np.random.random((2, 3))
