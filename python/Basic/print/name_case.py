#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 23:03:29/01/06/19
# Author  : Hugh Sun
# File    : name_case.py
# Software: name_case.py
name = input("What's your name?")
print("Hello",name,",","Would you like to learn some Python today?")


print(name,name.upper(),name.lower(),name.capitalize())
famous_person = "Albert Einstein"
message1 = "once said" 
message2 = "\"A person who never made a mistake never tried anything new.\""
message = message1 +","+ message2
print(famous_person + " once said," + message)
print(famous_person,"once said,",message) #difference abput + and ,
print("famous_person once said, \"A person who never made a mistake never tried anything new.\"")