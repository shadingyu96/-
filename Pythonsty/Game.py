from random import *


def fight():
    """
    人机战斗
    """
    # 定义自己的血量与随机攻击力150到250
    my_hp = 1000
    my_power = randint(150,250)
    # 定义敌人的血量与随机攻击力150到250
    enemy_power = randint(150,250)
    enemy_hp = 1000
    # 开始战斗直到自己或者敌人血量低于0时分出输赢
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp <= 0:
            print("你输了")
            break
        elif enemy_hp <= 0:
            print("你赢了")
            break
        else:
            # 战斗未结束，打印自己与敌人当前的血量
            print(f"正在战斗中...\n你剩余的血量:{my_hp}\n敌人剩余血量{enemy_hp}")


if __name__ == '__main__':
    fight()
