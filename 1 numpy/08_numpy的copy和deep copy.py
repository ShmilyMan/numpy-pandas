# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 10:10
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 06_numpy的array合并.py
# @Software: PyCharm
import numpy as np

a = np.arange(4)
# 将a赋值给b但并不使b和a进行关联
b = a.copy()    # deep copy
print(b)        # [0 1 2 3]