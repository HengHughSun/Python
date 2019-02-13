#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 15:36:41/02/12/19
# Author  : Hugh Sun
# File    : closure_return_function.py
# Software: 返回函数、闭包
#//////同一个返回函数对象(即return的是一个函数)，重复执行的时候，仅跑函数内的内容。返回函数外的内容是跑1次
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会change的变量。

def count():
    fs =[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs 

f1 , f2 , f3 = count()
print(f1(),f2(),f3())
#
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    f = [0]
    print('闭包外--')
    def counter():
        print('闭包内--')
        f[0] = f[0] + 1
        return f[0]
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


##内层函数能访问外层函数的变量，但不能修改它的指向

def createCounter():
    count = [0]
    def counter():
        count[0] += 1
        return count[0]
    return counter
##这种情况可行是因为count指向的是一个列表的实例对象，实质上，列表的实例对象的地址一直没变，只是其内容的指向改变了而已
      |
count[0]
count[1]
count[2] 地址没变-->变量没有改变
###而nonlocal关键字用来在函数或其他作用域中修改外层(非全局)变量

def createCounter():
    count = 0
    def counter():
        nonlocal count 
        count += 1
        return count
    return counter
###global关键字则是用于修改全局变量

#python引用变量的顺序： 当前作用域局部变量>>外层作用域变量>>当前模块中的全局变量>>python内置变量

