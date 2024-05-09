# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:43:41 2024

@author: USER
"""
# 利用for迴圈 計算1-100 奇數和
#加總能被7整除的數
#列出同時能被5和15整除的數
total = 0
Odd_total = 0

for i in range(1, 101, 1):
     if i%2 == 1:
         Odd_total+=i
     if i%7 == 0:
         total+=i
     if i%5 == 0 and i%15 == 0:
         print(i)
    
print("奇數和:", Odd_total)
print("被7整除之數的和:",total)
