#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 21:09:22/02/11/19
# Author  : Hugh Sun
# File    : sorted.py
# Software: sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
'''
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
reverse=True 实现反向排序
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(by_name(L))
L2 = sorted(L,key=by_name)
print(L2)
#按成绩降序排列
sorted_by_score = sorted(L, key=lambda s: s[1], reverse=True)
print(sorted_by_score)