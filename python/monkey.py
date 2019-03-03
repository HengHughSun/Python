#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 15:42:46/02/11/19
# Author  : Hugh Sun
# File    : monkey.py
'''Software: 这里有一个涵盖了我们所学所有知识的题目。你可能已经听说了无限猴子定理?该定理指出,猴
子随机在打字机键盘键入一个字符,经过无限时间后,肯定会键入一系列给定的文字,比如莎士比亚
全集。好吧,假设我们有一个 Python 函数替换猴子。你认为多久以后生成一句莎士比亚的名言?我们
将这句话定为:“methinks it is a weasel'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import string

def randomly_generate_string():
    generated_string = ''.join(random.sample(string.ascii_letters + ' '))
    return generated_string

def compare(source_string, target_string):
    best_match, best_match_length, worst_match, worst_match_length = 0.0, 100000000
    intersection = set(source_string) & set(target_string)
    convergence = set(source_string) | set(target_string)

    content_match = 1.0 * intersection / convergence
    if len(source_string) > len(target_string):
        length_match = 1.0 * target_string / source_string
    else:
        length_match = 1.0 * source_string / target_string

    # find best match string
    if content_match > best_match:
        best_match_string = source_string
        best_match = content_match
        best_match_length = length_match
    elif content_match == best_match:
        if length_match < best_match_length:
            best_match_string = source_string
            best_match_length = length_match

    # find worst match string


def main():
    flags = False
    content_match, length_macth = 0.0, 0.0
    while(not flags):
        source_string = 'methinks it is a weasel'
        generated_string = randomly_generate_string()
        flags = compare(source_string, generated_string)
