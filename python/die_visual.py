#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:20:07/01/12/19
# Author  : Hugh Sun
# File    : die_visual.py
# Software: die_visual.py
from die import Die 
import pygal
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sizes + die_2.num_sizes
for value in range(1,max_result + 1):
    frequnency = results.count(value)
    frequencies.append(frequnency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(2,max_result + 1))
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')

