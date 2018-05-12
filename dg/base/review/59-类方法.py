class Tool(object):
    count = 0
    def __init__(self, name):
        self.name = name
        # 类名.属性名 = xxx
        Tool.count += 1

    # 类方法，把获取count的方法封装在类里面
    @classmethod
    def show_tools_count(cls):
        print("工具的数量:%d" % cls.count)

tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("锯子")

Tool.show_tools_count()
