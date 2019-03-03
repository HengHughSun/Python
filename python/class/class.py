#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 22:53:11/01/09/19
# Author  : Hugh Sun
# File    : class.py
# Software: class = function + code body
# 类中的函数被称作为方法
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name and age"""
        self.name = name
        self.age = age 
        self.weight = 20
    #数据封装 
    def sit(self): 
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        print(self.name.title() + " roll over!")
    def current_weight(self,kg):
        if kg == 0:
            print('Error')
        else:
            self.weight = kg

my_dog = Dog('Willie',6)
print(my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old")
my_dog.roll_over()
print("My dog is " +str(my_dog.weight) + " kg")
my_dog.current_weight(10)
print("My dog is " +str(my_dog.weight) + " kg")


"""继承"""
class Car():
            #""" 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
    def get_descriptive_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()
    def read_odometer(self):
            print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
            self.odometer_reading += miles
class ElectricCar(Car):
        def __init__(self, make, model, year):
       # """ 初始化父类的属性 """
            super().__init__(make, model, year)#super()是一个特殊函数，讲父类和子类关联起来
        #    """父类也被称为supperclass"""
