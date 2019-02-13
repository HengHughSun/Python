#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 17:34:17/01/12/19
# Author  : Hugh Sun
# File    : rw_visual.py
# Software: rw_visual.py
import matplotlib.pyplot as plt 

from randomWalk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()

     #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))#函数 figure() 用于指定图表的宽度、高度、分辨率和背景色
    #dpi=XX向figure()传递分辨率


    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
    edgecolors='none',s=50)
    
    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
    
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

   
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break