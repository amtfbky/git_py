"""not to write in chinese sublime-text?"""
class Home:
    
    def __init__(self,new_area,new_model,new_addr):
        self.area = new_area
        self.model = new_model
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        
        return ("房子的总面积：%d，可用面积是：%d，户型是：%s，地址是：%s，家具有：%s"
            % (self.area,self.left_area,self.model,self.addr,str(self.contain_items)))

    def add_item(self,item):
        #self.left_area -= item.area
        #self.contain_items.append(item.name)

        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    
    def __str__(self):
        return "%s所占的面积：%d"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name


fz = Home(130,"三室一厅","劈才胡同")
print(fz)

bed1 = Bed("席梦思",4)
fz.add_item(bed1)
print(fz)

bed2 = Bed("三人床",6)
fz.add_item(bed2)
print(fz)
