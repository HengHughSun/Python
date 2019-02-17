#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 15:54:47/01/23/19
# Author  : Hugh Sun
# File    : lambda.py
# Software: 匿名函数相当设定预设值small anonymous function
#lambda can take any number of arguments, but can only have one expression.
"""syntax ： lambda arguments : expression 关键字lambda表示匿名函数，冒号前面的x表示函数参数"""
x = lambda a : a + 5
a = 6
print(x(a))
x = lambda a, b : a * b 
print(x(5,6))

#当您将lambda用作另一个函数内的匿名函数时，会更好地显示lambda的强大功能。

#假设您有一个带有一个参数的函数定义，并且该参数将乘以未知数字：

#使用该函数定义来创建一个总是使您发送的数字加倍的函数：
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
#在短时间内需要匿名函数时使用lambda函数。

#也可以把匿名函数作为返回值返回，比如：

def build(x, y):
    return lambda: x * x + y * y