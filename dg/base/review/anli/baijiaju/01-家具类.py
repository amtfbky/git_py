# 重要的步骤单独存档
# 第一步：设计家具类

class HouseItem:
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f。" % (self.name, self.area)


# 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

# 显示家具信息
print(bed)
print(chest)
print(table)
