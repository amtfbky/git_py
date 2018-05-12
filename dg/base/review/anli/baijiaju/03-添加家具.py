# 重要的步骤单独存档
# 第一步：设计家具类
# 第二步：设计房子类
# 第三步：添加家具
# 这里一个知识点：参数item是家具的引用

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
        print("要添加的家具是：%s" % item)

        # 1.判断家具面积是否>剩余面积
        if item.area > self.feel_area:
            # 如果>，则提示
            print("您要添加的家具面积过大，请更换家具！")
            return
        # 2.减除家具面积
        self.feel_area -= item.area

        # 3.将家具放到家具列表
        self.item_list.append(item.name)

# 创建家具对象
bed = HouseItem("席梦思", 39)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)

# 创建房子对象
house = House("两室一厅", 40)
# 添加家具，把家具的引用当参数传到添加方法里
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
# 显示添加家具后房子信息
print(house)
