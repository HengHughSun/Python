#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 13:58:16/01/07/19
# Author  : Hugh Sun
# File    : dictionary.py
# Software: dictionary.py
#字典和list的不同之处在于字典存储的是键值对
#函数名 使用方法         解释
#keys adict.keys()     以列表的形式返回 adict 中的所有键(key)
#values adict.values() 以列表的形式返回 adict 中的所有值(value)
#items adict.items()   以列表的形式返回 adict 中的所有键值对,列表的每个元素是包含键和值的元组
#get adict.get(key)    返回 key 所对应的值,如果 key 不存在,就返回 None
#get adict.get(key,alt)返回 key 所对应的值,如果 key 不存在,就返回 alt
#-----------python 中字典中的函数操作
#
alien_0 = {'colour':'green','point':5}
print(alien_0['colour'])
print(alien_0['point'])

person = {
            'first_name':'Heng',
            'last_name':'Sun',
            'age':'22',
            'city':'Zhengzhou',
            }
for i,q in person.items():
    print("\nKey: " + i)
    print("Value: " + q)

favorite_languages = {
            'jen': 'python',
            'sarah': 'c',
            'edward': 'ruby',
            'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title() + ", thank you for taking the poll.")
