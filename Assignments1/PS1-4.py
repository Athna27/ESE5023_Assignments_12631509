# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:59:26 2026

@author: 22521
"""

#假设你最初有 1 元人民币，每次操作时，你可以选择将钱翻倍或再增加 1 元人民币。要使最终金额正好达到 x 元人民币，你至少需要进行多少次操作？这里 x 是从 1 到 100 之间随机选取的整数。编写一个函数 Least_moves 来输出结果。例如，Least_moves(2) 应输出 1，Least_moves(5) 应输出 3
#这个一开始没有思路 有检索网页和咨询AI 得到反向推算的思路
import random
x  = random.randint(1, 100)
def Least_moves(x):
    n = 0
    while x > 1:
        if x % 2 == 0: #x/2的余数是零，即x是偶数
            x = x // 2 #此处对结果取整，/2得到的结果可能是小数，//2得到的是整数
        else:
            x = x - 1
        n = n + 1
    return n
    print(n)
Least_moves(x)
