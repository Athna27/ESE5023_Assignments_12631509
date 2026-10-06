# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:12:22 2026

@author: 22521
"""

# 最有趣的数字模式之一是帕斯卡三角形（以布莱兹·帕斯卡命名）。编写一个名为 Pascal_triangle 的函数，该函数接受一个参数 k，用于输出帕斯卡三角形的第 k 行。请输出 Pascal_triangle(100) 和 Pascal_triangle(200) 的结果。
#我的思路是第0行是0，1，0，第1行是0，1，1，0，第k行第n个数是第k-1行的第n-1和第n个数的和
k = int(input("Please enter k: "))
def Pascal_triangle(k):
    row = [1]
    for i in range(1, k+1):
        old_row = [0] + row + [0]
        new_row = []
        for n in range(len(old_row) - 1):
            new_row.append(old_row[n] + old_row[n + 1])    
        row = new_row
    return row
#需要输出调用函数后的结果，一开始只是print（row）,输出结果是之前有问题的代码定义的全局变量，不会受k值影响
print(Pascal_triangle(k))

#k=100和k=200可直接在input处输入得到