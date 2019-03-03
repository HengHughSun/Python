#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:08:47/01/05/19
# Author  : Hugh Sun
# File    : list.py
# Software: list.py arrary learn knowladge
#list tuple string 都可以slice切片


#名称     运算符  讲解
#索引     [ ]    指向序列中的一个元素
#连接      +     组合序列
#重复      *     重复该序列
#是否在其中 in    查询该元素是否在序列中
#长度     len    获取序列长度
#切片     [ : : ]  切片操作 Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片,支持步数切片[::-1]倒着取出序列
#>>> myList = [0] * 6
#>>> myList
#[0, 0, 0, 0, 0, 0]
#>>> mylist = [1,2,3,4]
#>>> A = [mylist]*3
#>>> print(A)
#[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
#>>> mylist[2]=45
#>>> print(A)
#[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
#>>> mylist
#[1, 2, 45, 4]
#>>> A
#[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
#变量A持有拥有三份对原始名为mylist序列的引用的容器。注意在对mylist中的元素进行改变后,这种改变体现在了A中。
#方法名  用法                  解释
#append alist.append(item)   在列表末尾添加一个新项
#insert alist.insert(i,item) 在列表的某个位置插入一个项
#pop    alist.pop()          移除并返回列表的最后一项
#pop    alist.pop(i)         移除并返回列表的第 i 项
#sort   alist.sort()         对列表进行排序
#reverse alist.reverse()     反转列表
#del     del alist[i]        删除在该位置上的元素
#index  alist.index(item)    返回列表中第一个等于 item 项的索引
#count  alist.count(item)    返回列表中有多少项的值等于 item
#remove alist.remove(item)   删除列表中第一个值等于 item 的项

#
#-----string 字符串
#rstrip(),lstrip() 和 strip() 剔除后面、前面、前后的空白
#upper()          # 把所有字符中的小写字母转换成大写字母
#lower()          # 把所有字符中的大写字母转换成小写字母
#capitalize()     # 把第一个字母转化为大写字母，其余小写,即整句话的首字母大写
#title()          # 把每个单词的第一个字母转化为大写，其余小写，即每个单词的首字母大写
#replace("","")   # 从X字符替换为Y字符
#split(",")       # 如果找到分隔符的实例，将字符串拆分为子字符串myName = David, myName.split('v'), ['Da', 'id']
#center(w)        # 返回一个字符串,w 长度,原字符串居中
#ljust(w)         #居左
# rjust(w)        #居右  
#find('')         #查询 item,返回第一个匹配的索引位置  等同与list.index('')
#count(item)      #返回item出现的次数
#----list 
#///range(101)相当于range(0,101)生成的序列是从0开始小于101的整数：==sequence Shell：seq((0..100)) 
#//range()还可以指定步长range(0,101,2)生成的序列是从0开始小于101的偶数，步数支持负数 注意range只是生成数据 引用需要赋值
#Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
#
#字符串和列表之间最大的区别就是列表可以被修改而字符串不行。这被称作易变性。列表是可变的,字符串时不可变的。
#元组tuple类似字符串，都是不可变数据类型：
classmates = ['Michael','Bob','Tracy','May','John']

print(classmates)
print(len(classmates))

print(classmates[0:2])   #切片输出【0：2】表示第1个和第2个元素被输出MB  
#【1：4】表示第2个第3个和第4个TM要提取列表的第 2~4 个元素,可将起始索引指定为 1 ,并将终止索引指定为 4
print("qiebian")
#rint(len(classmates))
#classmates[0]=Michael  classmates[2]=Tracy 
#classmates[-1]=Tracy   clasmates[-3]=Michael
classmates.append('Hugh') #追加
classmates.insert(1,'Jack')
i = classmates.index('Hugh') #取索引值
print(classmates)
print(i)
print(len(classmates))
#classmates.pop() #method方法，类函数pop -->删除元素 （i）删除制定位置的元素,可以将值赋给 新变量 来再次使用
classmates[1] = "Sarach" #直接赋值完成 替换
del classmates[1] #del语句 --> 删除元素
print(classmates)
print(len(classmates))
#如果你不确定该使用 del 语句还是 pop() 方法,
# 下面是一个简单的判断标准:如果你要从列表中删除一个元素,且不再以任何方式使用它,就使用 del 语句;
# 如果你要在删除元素后还能继续使用它,就使用方法 pop()
#有时候,你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值,可使用方法 remove() 。限制：只能删除匹配到的第一个值
classmates.remove('Bob')
#数组可以加数组 即不同维度的数组
print(classmates)
print(len(classmates))

classmates.insert(1,'Alice')
classmates.append('Bob')
print("\nHere is the sorted list:")
print(sorted(classmates))#sorted()临时改变数组
print(classmates)
print(len(classmates))

classmates.sort(reverse=True)#永久改变数组  reverse=True reverse() 不是指按与字母顺序相反的顺序排列列表元素,而只是反转列表元素的排列顺序

print(classmates)
print(len(classmates))