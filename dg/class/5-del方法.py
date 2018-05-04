class Zero:
    def __del__(self):
        print("-------Zero over-----------")


zero1 = Zero()
zero2 = zero1
#zero3 = zero1
# 这一句删除英雄1，好比硬链接的链接数从2变成了1
del zero1
"""
=========
zero over"""
# 这一句删除英雄2，好比硬链接的链接数从1变成了0，很多游戏里角色死了会一声惨叫或者其他动作表现什么的
# 这就是del函数内置的执行动作
del zero2
"""
zero over
=========
"""
#del zero3
print("=========")
