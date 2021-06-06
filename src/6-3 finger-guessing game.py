"""
猜拳游戏
"""

import random

print("猜拳游戏：")
print("0：石头")
print("1：剪刀")
print("2：布")
print("3：退出")
print("-------------------------")
while True:
    player=int(input("请输入一个数字"))
    if player==3:
        print("----------------------")
        print("感谢游玩~")
        print("----------------------")
        break;
    
    computer=random.randint(0,2)
    list=["石头","剪刀","布"]
    print("你出的%s，电脑出的%s" % (list[player],list[computer]))
    if player-computer==-1 or player-computer==2:
        print("你赢了")
    elif player==computer:
        print("平手")
    else:
        print("你输了")
    print()