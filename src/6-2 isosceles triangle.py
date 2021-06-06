"""
打印等腰三角形
"""

#写法一
for i in range(10):
    for j in range(0, (10 - i)):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")
    print("")

#写法二（简化写法）
for i in range(10):
    print(" " * (10-i), end="")
    print("* " * (i), end="")
    print()