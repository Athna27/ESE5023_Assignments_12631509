# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:44:29 2026

@author: 22521
"""
#Flowchart:Write a function Print_values with arguments a, b, and c to reflect the following flowchart. Here the purple parallelogram operator is to print values in the given order. Report your output with some random a, b, and c values.
#导入随机数，赋值并通过if/else判断后从大到小对a,b,c进行排序
import random
a = random.random()
b = random.random()
c = random.random()
def Print_values(a,b,c):
    if a > b:
        if b > c:
            print(a,b,c)
        else:
            if a > c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b <= c:
            print(c,b,a)
print("a, b, c =", a, b, c)
Print_values(a, b, c)
