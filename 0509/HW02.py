# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:21:49 2024

@author: USER
"""

# 由使用者輸入a,b,c三邊，判斷是不是三角形，是的話再判斷是不是直角三角形

a = int(input("請輸入邊長a:"))
b = int(input("請輸入邊長b:"))
c = int(input("請輸入邊長c:"))

if a+b>c and a+c>b and b+c>a:
    print("是三角形")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print("也是直角三角形")
    else:
        print("不是直角三角形")
else:
    print("不是三角形")

