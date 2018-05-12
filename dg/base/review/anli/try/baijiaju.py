class Item:
    """家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s's area is %.2f." % (self.name, self.area)


class House:
    """房子类"""

    def __init__(self, model, area):
        self.model = model
        self.area = area
        self.feel_area = area
        self.item_list = [] # 用来记录家具

    def __str__(self):
        # 家具列表是可以直接输出的
        return ("model:%s\narea:%d\nfeel_area:%.2f\nitem_list:%s" % 
                (self.model, self.area, self.feel_area, self.item_list))

    def add_item(self, item): 
        print("add:%s" % item)

        # 1.判断家具的面积，如果家具面积>剩余面积，则返回
        if item.area > self.feel_area:
            # 如果家具面积超过剩余面积，这里要提示
            print("%s's area not in the house." % item.name)
            return

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)

        # 3.计算剩余面积
        self.feel_area -= item.area


bed = Item("xms", 38)
chest = Item("chest", 4)
table = Item("table", 2.5)

house = House("3room1ting", 40)
# 这里要调用添加家具的方法，并把家具对象的引用bed当参数传入方法
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
# 这里显示house要在添加家具之后
print(house)
