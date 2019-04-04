#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 19:53:26/02/22/19
# Author  : Hugh Sun
# File    : data.py
# Software: 一个函数 CheckDate(date)，给定任意日期date，算出该日期是否超过了date所在月份的第三个周五。
# 例：CheckDate(“20180725”) -> true; CheckDate(“20180103”) -> false

import datetime
import calendar

class Solution:
    def CheckDate(self,cal):
        def Diff(newday):
            print(day)
            print(newday)
            if day > newday:
                return print("True")
            else:
                return print("False")
        
        
        year = int(cal[:4])
        month = int(cal [4:6])
        day = int(cal[6:8])
        now = datetime.date(year,month,1)
        week = now.weekday()
        if week == 4:
            newday = 15 
            Diff(newday)
        elif week > 4:
            newday = 22 - week + 4 
            Diff(newday) 
        elif week < 4:
            newday = 15 + 4 - week 
            Diff(newday)


if __name__ == "__main__":
    x = Solution()
    x.CheckDate("20180725")


