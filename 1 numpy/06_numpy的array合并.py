# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 10:10
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 06_numpy的array合并.py
# @Software: PyCharm
import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])
# 1.横向的合并
print(np.hstack((a,b)))     # [1 1 1 2 2 2]
# 2.纵向的合并
'''
    [[1 1 1]
    [2 2 2]]
'''
print(np.vstack((a,b)))
# 3.增加横向的维度
print(a[np.newaxis,:])      # [[1 1 1]]
# 4.增加纵向的维度
'''
    [[1]
    [1]
    [1]]
'''
print(a[:,np.newaxis])
