#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:24:21/01/05/19
# Author  : Hugh Sun
# File    : tuple.py
# Software: tuple.py 元组 与list非常类似，但不允许后续修改
#[]表示list  ()表示tuple
#因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
#
#>>> t = (1,)
#>>> t
#(1,)
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。


#tuple 里可以有list  以此可以实现可以变化的tuple