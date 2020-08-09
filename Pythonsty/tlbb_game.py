from random import *
from Shadingyu.Pythonsty.tlbb import *

tl_hp = 5000
tl_power = randint(100, 300)
tl = TongLao("佛山童姥", tl_hp, tl_power)
tl.see_people("无崖子")
tl.see_people("李秋水")
tl.see_people("丁春秋")
tl.see_people("马云")

tl.fight_zms()
enemy_hp = 6000
enemy_power = randint(200, 250)
tl.fight_enemy(enemy_hp, enemy_power)


print("-" * 50)
xz = XuZhu("虚竹", 5000, 200)
xz.fight_zms()
xz.fight_enemy(500, 2009)
