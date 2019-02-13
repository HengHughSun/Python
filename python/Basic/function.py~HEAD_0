#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 21:40:45/01/07/19
# Author  : Hugh Sun
# File    : function.py
# Software: function.py
#-----------函数
#--可变的实参，都需要跟在‘位置参数’后面
#----任意数量的实参（*function_key）可变参数
#        一个key可以接受多个value 返回的是值
#----关键字参数(**fuction_key)  **相当于创建了个字典:
#       可以接受多个键值对，一个key对应一个value 返回的是键值对
#----命名关键字参数(*,function_key,function_key)
#       同上，只不过多了default值 返回的是值
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#(a, b, c=0, *args, **kw)ab必选参数，c默认参数，args可变参数，关键字参数
#a, b, c=0, *, d, **kw） *，d命名关键字参数 
#这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def sandwich(*toppings):
    print ('There is you sanwich with')
    for topping in toppings:
        print('-'+topping)
sandwich('onion','meat','beef')
sandwich('leak')
sandwich('wudi','meichaofeng')

from collections import OrderedDict
def car_info(first,last,**car_infos):
    info = OrderedDict()
    info['firstname'] = first
    info['lastname'] = last
    for key,value in car_infos.items():
        info[key] = value
    return info
car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')