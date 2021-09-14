# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 14:24
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 04_numpy的基础运算2.py.py
# @Software: PyCharm
import numpy as np

a = np.arange(2,14).reshape((3,4))
# 1.计算最小值和最大值的索引(索引从0开始)
'''
    [[ 2  3  4  5]
    [ 6  7  8  9]
    [10 11 12 13]]
'''
print(np.argmin(a),np.argmax(a))            # 0 11
# 2.计算平均值
print(np.mean(a),a.mean(),np.average(a))    # 7.5 7.5 7.5
# 3.求中位数
print(np.median(a))                         # 7.5
# 4.前缀和
print(np.cumsum(a))         # [ 2  5  9 14 20 27 35 44 54 65 77 90]
# 5.累差
'''
    [[1 1 1]
    [1 1 1]
    [1 1 1]]
'''
print(np.diff(a))
# 6.排序：逐行逐行的排序，从小到大
'''
    [[ 2  3  4  5]
    [ 6  7  8  9]
    [10 11 12 13]]
'''
print(np.sort(a))
# 7.矩阵的转置
'''
    [[ 2  6 10]
    [ 3  7 11]
    [ 4  8 12]
    [ 5  9 13]]
'''
print(np.transpose(a))
# 8.矩阵的截取
'''
    [[5 5 5 5]
    [6 7 8 8]
    [8 8 8 8]]
'''
print(np.clip(a,5,8))       # 所有小于5的数都让他变成5，所有大于8的数都让他变成8