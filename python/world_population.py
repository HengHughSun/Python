#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 12:52:51/01/13/19
# Author  : Hugh Sun
# File    : world_population.py
# Software: world_population.py
import json
from countries_pygal import get_country_code
import pygal.maps.world 
from pygal.style import LightColorizedStyle,RotateStyle

with open ("./python/population_data.json") as pd:
    pop_date = json.load(pd)



cc_populations = {}
"""打印每个国家2010年的人口数量"""
for pop_dict in pop_date:
    if pop_dict['Year'] == "2010":
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            #print(code + ": "+ str(population))
            
            #创建一个包含人口数量的字典
            cc_populations[code] = population
        #else:
         #   print("Error -"+ country_name)
vm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
vm = pygal.maps.world.World(style=vm_style)
vm.title = 'World Population in 2010. by Country'
vm.add('In 2010',cc_populations)

vm.render_to_file('world_population.svg')
