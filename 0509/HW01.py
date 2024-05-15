# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:08:15 2024

@author: USER
"""

# 亂數產生5~100之間可以被5整除的數，產生5個且不可重複(用5個變數儲存)

import random

one = random.randrange(5,101,5)
two = random.randrange(5,101,5)
while two == one:
    two = random.randrange(5,101,5)
three = random.randrange(5,101,5)
while three == one or three == two:
    three = random.randrange(5,101,5)
four = random.randrange(5,101,5)
while four == one or four == two or four == three:
    four = random.randrange(5,101,5)
five = random.randrange(5,101,5)
while five == one or five == two or five == three or five == four:
    five = random.randrange(5,101,5)

print(one)
print(two)
print(three)
print(four)
print(five)
    
    
    