# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 10:10
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 06_numpy的array合并.py
# @Software: PyCharm
import numpy as np

a = np.arange(12).reshape(3,4)
'''
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
'''
# axis=0    横向分割    axis=1  纵向分割
print(np.split(a,3,0))      # 均匀的分割
'''
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
'''
print(np.array_split(a,2,0))      # 不均匀的分割

# 分割的另一种方法（均匀不均匀均可）
print('--------------------------')
'''
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
'''
print(np.vsplit(a,3))   # 横向


'''
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
'''
print(np.hsplit(a,2))   # 纵向