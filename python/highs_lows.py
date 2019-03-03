#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 22:30:54/01/12/19
# Author  : Hugh Sun
# File    : highs_lows.py
# Software: highs_lows.py
import csv
from datetime import datetime
from matplotlib import pyplot as plt 

filename = "./python/sitka_weather_2014.csv"
with open(filename) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)
    
#   for index, column_header in enumerate(header_row):#enumerate()来获取每个元素的索引及其值
#        print(index, column_header)
    dates, highs ,lows = [] ,[] ,[]
    for row in reader:
        try:
           current_date = datetime.strptime(row[0],"%Y-%m-%d")
           high = int(row[1])
           low = int(row[2])
        except ValueError:
           print(current_date, "missing data") 
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
"""绘制图形"""
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')

plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.5)
#fill_between() ,它接受一个 x 值系列和两个 y 值系列,并填充两个 y 值系列之间的空间,alpha调深浅

plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制斜的日期便签
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()