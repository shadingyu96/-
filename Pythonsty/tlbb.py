import time


class TongLao:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    @staticmethod
    def see_people(name):
        # 看见不同的人时说不同的话
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("路过，我不认识你")

    def fight_zms(self):
        # 使用天山折梅手技能，血量减少一倍，攻击力增加一倍。
        self.power = self.power * 10
        self.hp = self.hp / 2
        print(f"{self.name}使用了天山折梅手，现在{self.name}的血量是{self.hp},攻击力是{self.power}")

    def fight_enemy(self, enemy_hp, enemy_power):
        # 与敌人打架
        while True:
            self.hp -= enemy_power
            enemy_hp -= self.power
            if self.hp <= 0:
                print("你死了，打不过敌人")
                break
            elif enemy_hp <= 0:
                print("敌人被你干死了，你好厉害")
                break
            else:
                print(f"战斗还在继续，{self.name}的血量{self.hp}|{self.name}的攻击力{self.power}\t"
                      f"敌人的血量{enemy_hp}|敌人的攻击力{enemy_power}")
                time.sleep(0.5)


class XuZhu(TongLao):
    @staticmethod
    def read():
        print("罪过罪过")

    def fight_enemy(self, enemy_hp, enemy_power):
        # 与敌人打架
        self.read()


# if __name__ == '__main__':
#     tl = TongLao(500, 20)
#     tl.see_people("WYZ")
#     tl.fight_zms()
#     xz = XuZhu(500, 200)
#     xz.read()
