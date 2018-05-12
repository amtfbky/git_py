# 重要的步骤单独存档
# 第一步：设计家具类
# 第二步：设计房子类

class HouseItem:
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f。" % (self.name, self.area)


class House:
    """房子类"""

    def __init__(self, model, area):
        self.model = model
        self.area = area
        # 剩余面积，先=房子的总面积
        self.feel_area = area

        # 家具列表，先是空的
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具：%s" % 
                (self.model, self.area, self.feel_area, self.item_list))

    def add_item(self, item):
        # 这个item参数可神奇了
        # 它可以把家具的信息显示出来=print(家具名称)
        print("要添加的家具是：%s" % item)

# 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

# 创建房子对象
house = House("两室一厅", 40)
# 试一下添加家具方法，把家具的引用当参数传到添加方法里
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
# 显示房子信息
print(house)
