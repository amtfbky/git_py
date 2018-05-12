class Tool(object):
    count = 0
    def __init__(self, name):
        self.name = name
        # 类名.属性名 = xxx
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("锯子")

print(tool3.count)
tool3.count = 9
# 对象名.属性名 = xxx
print(tool3.count)

print(Tool.count)
