class Tool(object):
    # 类属性
    num = 0
    # 方法
    def __init__(self,new_name):
        # 实例属性
        self.name = new_name
        # 对类属性+=1
        Tool.num += 1

tool1 = Tool("铁锹")
tool2 = Tool("兵工铲")
tool3 = Tool("水桶")
print(Tool.num)
"""创建对象开辟一个内存空间：存储对象的属性
注意点：
    有个特殊的属性：能够知道这个对象的class
    比如一辆车哪里都能显示这个车类的信息
    
    类在面向对象里也是对象，类对象
    实例对象
    
    实例属性的特点：
        和具体的某个实例对象有关系
        并且实例对象之间不共享属性
    类属性的特点：
        属于类对象
        多个实例对象之间共享类属性"""
