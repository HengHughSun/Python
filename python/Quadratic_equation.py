#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 23:04:49/01/05/19
# Author  : Hugh Sun
# File    : 一元二次方程.py
# Software: 一元二次方程.py
import math 
def quadratic(a,b,c):
    if a == 0:
        raise TypeError('a不能为0')
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    mid = b**2 - 4 * a * c
    if mid > 0 :
        x1 = -b + math.sqrt(mid)/(2*a)
        x2 = -b - math.sqrt(mid)/(2*a)
        return x1,x2
    elif mid == 0:
        x1,x2 = -b + math.sqrt(mid)/(2*a)
    else:
        print('方程无实数根')
a = int(input("Type number:"))

b = int(input("Type number:"))
c = int(input("Type number:"))


print(quadratic(a,b,c))
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d))/2/a 
            x2 = (-b - math.sqrt(d))/2/a
            return x1,x2        
print(quadratic(2,3,1))
print(quadratic(1,3,-4))


