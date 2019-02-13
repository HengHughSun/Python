#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:15:02/01/12/19
# Author  : Hugh Sun
# File    : die.py
# Software: die.py
from random import randint
class Die():
    
    def __init__(self,num_sizes=6):
        """骰子默认为6面"""
        self.num_sizes = num_sizes
    
    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sizes)