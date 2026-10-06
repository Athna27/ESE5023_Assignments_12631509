# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:11:17 2026

@author: 22521
"""

#Matrix multiplication：2.1 [5 points] Make two matrices M1 (5 rows and 10 columns ) and M2 (10 rows and 5 columns ); both are filled with random integers from 0 and 50；2.2 [10 points] Write a function Matrix_multip to do matrix multiplication, i.e., M1 * M2. Here you are ONLY allowed to use for loop, * operator, and + operator.
#2.1
#此处检索了如何创建随机数矩阵：
import numpy as np
n1 = np.random.randint(0,50,(5,10))
n2 = np.random.randint(0,50,(10,5))
print(n1,n2)

#2.2
#定义n3是n1*n2，n3是5行5列
n3 = np.zeros((5,5))
def Matrix_multip(n1,n2):
    for i in range(5):      #对于n1中的5行
        for j in range(5):  #对于n2中的5列
            for k in range(10): #k代表n3某个位置上有k个乘积相加
                n3[i][j] = n3[i][j] + n1[i][k] * n2[k][j]
    return n3  #没有返回n3的话得到的是none...

n3 = Matrix_multip(n1,n2)
print(n3)           
