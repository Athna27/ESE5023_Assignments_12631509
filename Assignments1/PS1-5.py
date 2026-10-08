# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:59:36 2026

@author: 22521
"""

#在数字 123456789 之间的任意位置插入 + 或 - 运算符，使该表达式计算结果为一个整数。你可以将数字组合起来形成更大的数，但数字的顺序必须保持不变。
#5.1 [30 分] 编写一个函数 Find_expression，该函数应能输出所有可能的解，使得该表达式计算结果为 1 到 100 之间的任意整数。例如，Find_expression(50) 应输出包含以下内容的行：1−2+34+5+6+7+8−9=50以及1+2+34−56+78−9=50
def Find_expression(target, show=True):
    count = 0
    def search(index, total, current, expression):
        nonlocal count

        if index == 10:
            if total + current == target:
                count = count + 1

                if show:
                    print(expression, "=", target)

            return
        digit = index
        # 选择1：+
        search(index + 1,
               total + current,
               digit,
               expression + "+" + str(digit))
        # 选择2：-
        search(index + 1,
               total + current,
               -digit,
               expression + "-" + str(digit))
        # 选择3：连接数字
        if current >= 0:
            connected = current * 10 + digit
        else:
            connected = current * 10 - digit

        search(index + 1,
               total,
               connected,
               expression + str(digit))

    search(2, 0, 1, "1")

    return count

Find_expression(50)

#5.2
import matplotlib.pyplot as plt

Total_solutions = []

for x in range(1, 101):
    number = Find_expression(x)
    Total_solutions.append(number)

print(Total_solutions)

plt.plot(range(1, 101), Total_solutions)

plt.xlabel("Target integer")
plt.ylabel("Number of solutions")
plt.title("Number of solutions from 1 to 100")

plt.show()

maximum = max(Total_solutions)
minimum = min(Total_solutions)

print("Maximum =", maximum)
print("Minimum =", minimum)

for i in range(100):
    if Total_solutions[i] == maximum:
        print("Maximum occurs at x =", i + 1)

for i in range(100):
    if Total_solutions[i] == minimum:
        print("Minimum occurs at x =", i + 1)
        
        
        
        
        
        
        
        
        
        
        
        