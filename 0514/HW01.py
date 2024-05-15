# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:06:33 2024

@author: USER
"""

"""
課後練習
1-1 黑名單:10,15,39 不可以被新增進去
1-2 請使用random的方式來自動新增六個數字 範圍1-49
1-3 白名單:17,41一定要有
"""
import random

number = list()

blacklist = [10, 15, 39]
whitelist = [17, 41]

#先把白名單中的數字加入
for num in whitelist:
    number.append(num)


while len(number) < 6:
    num = random.randrange(1, 50)
    #如果num在黑名單中有或是在number裡有就跳過
    if num in blacklist or num in number:
        continue
    number.append(num)

#打亂列表順序以確保白名單數字位置隨機
random.shuffle(number)


print(number)
    
