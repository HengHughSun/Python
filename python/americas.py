#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 17:50:00/01/13/19
# Author  : Hugh Sun
# File    : americas.py
# Software: world_population.py

from pygal.maps.world import World

wm = World()
wm.title = "North, Central, and South America" 


#方法add 接受一个标签和一个列表
wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl',
'co','ec','gf','gy','pe','py','sr','uy','ve'])
wm.render_to_file('america.svg')
