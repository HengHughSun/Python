#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 19:28:00/02/12/19
# Author  : Hugh Sun
# File    : decorator.py
# Software: decorator装饰器  @用法 @log 相当于now = log(now)  now(变量) @log('execute') == now = log('execute')(now)

import time, functools
'''计算时间'''
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        f = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - start))
        return f
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
#相当于fast = metric(fast)
#        fast(x,y)
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

'''log 记录record'''

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
            # print('calling func: %s' % func.__name__)
            print(" call %s" % (func.__name__)) 
            f = func(*args, **kw)
            print('end call')
            return f
        return wrapper
    return decorator if isinstance(text, str) else decorator(text)
# 
'''def log(text): *关键字函数和位置函数的区别('execute',) now():    execute now():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator   '''

@log
def now():
    pass

now()

@log('execute')
def g():
    pass

g()
