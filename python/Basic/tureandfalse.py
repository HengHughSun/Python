#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 13:06:26/01/07/19
# Author  : Hugh Sun
# File    : tureandfalse.py
# Software: conditional_test 条件测试
cars = ['bwm','audi','toyota','subara']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


numbers = range(1,10)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + "th")