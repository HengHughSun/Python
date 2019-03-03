#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 15:31:14/01/07/19
# Author  : Hugh Sun
# File    : test1.py
# Software: test1.py
# 创建一个用于存储外星人的空列表
aliens = []
# 创建 30 个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#前3个为黄色的中速的外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))