#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 12:55:35/01/12/19
# Author  : Hugh Sun
# File    : mpl_squares.py
# Software: matplotlib_squares
import matplotlib.pyplot as plt 
input_values = [1,2,3,4,5]#设定x轴默认从0开始
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)#linewidth绘制的线条的粗细
"""设置图标标题，并给坐标轴加上标签"""
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()


""""scatter()散点图"""
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
"""plt.scatter(x_value,y_value,c='red',edgecolor='none',s=40)"""#edgecolor='none'删除数据点的轮廓
#参数c自定义颜色，支持RGB颜色模式（三原色）c=(0,0,0.8)值越接近0，颜色越深 1 越浅
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,edgecolor='none',s=40)
#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24) 
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()
