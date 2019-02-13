#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:44:58/01/05/19
# Author  : Hugh Sun
# File    : test.py
# Software: test.py
sum = 0
for i in range(101):
    sum = sum + i
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)
i=len(L)
while i < 3 :
    print(L[i])
    i = i-1
    if i > 2 :
        break
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-54))

<<<<<<< HEAD
def product(x,*y):
    if not y:
        return x 
    else:
        for i in y:
            x = x * i
        return x 
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
=======
def product(x,y=1,*z):
    return x * y * z
print(product(1,y=2,z=4))
>>>>>>> first add
