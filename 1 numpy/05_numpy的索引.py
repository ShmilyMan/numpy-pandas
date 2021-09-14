# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 20:23
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 05_numpy的索引.py
# @Software: PyCharm
import numpy as np

a = np.arange(0,12).reshape((3,4))
'''
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
'''
# 通过索引取值,索引从0开始
print(a[1])             # 第一行的值    [4 5 6 7]
print(a[1][1])          # 第一行第一列的值  5
print(a[1,1])           # 第一行第一列的值  5
print(a[1,:])           # 第一行的值    [4 5 6 7]      :代表取所有的值
print(a[:,1])           # 第一列的值    [1 5 9]

# 1.迭代输出每一行
print('----------------')
for row in a:
    print(row)
# 2.迭代输出每一列
print('----------------')
for col in a.T:
    print(col)
# 3.输出每个元素值
print('--------1--------')
for item in a.flat:
    print(item)
print('--------2--------')
for row in a:
    for item in row:
        print(item)