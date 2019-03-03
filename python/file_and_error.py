#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:41:16/01/10/19
# Author  : Hugh Sun
# File    : file_and_error.py
# Software: file_and_error.py
with open('./python/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
file_name = "/home/heng/learn/python/pi_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""ZeroDivisionError"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    try:
        answer = round((int(first_number) / int(second_number)),3)
    except ZeroDivisionError:
        print("you can't division by 0!")
    else:
        print(answer)

"""FileNotFoundError"""
file_name = "/home/heng/learn/python/Introduction_to_the_study_of_the_history_of_language.txt"
try:
    with open(file_name,'r') as f_obj:
        contents = f_obj.read()
except:
    msg = "Sorry, the file " + file_name + " doesn't exist."
    print(msg)
else:
    """计算文件大致包含多少个单词"""
    words = contents.split()
    num_words = len(words)
    print("The file" + file_name + " has about " + str(num_words) + " words.")
"""TypeError"""