class SweetPotato:

    def __init__(self):
        self.cookedString = "生的"
        self.cookeLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜状态：%s(%d，添加作料：%s)"%(self.cookedString,self.cookeLevel,str(self.condiments))

    def cook(self,cooked_time):
        self.cookeLevel += cooked_time
        if self.cookeLevel >= 0 and self.cookeLevel < 3:
            self.cookedString = "生的"
        elif self.cookeLevel >= 3 and self.cookeLevel < 5:
            self.cookedString = "半生不熟"
        if self.cookeLevel >= 5 and self.cookeLevel < 8:
            self.cookedString = "熟了"
        if self.cookeLevel > 8:
            self.cookedString = "烤糊了"
    
    def addCondiments(self,item):
        self.condiments.append(item)

digua = SweetPotato()
digua.cook(int(input("time: ")))
zuoliao = input("zuoliao: ")
digua.addCondiments(zuoliao)
print(digua)

"""
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)

digua.addCondiments("番茄酱")
print(digua)
digua.cook(1)
digua.addCondiments("孜然")
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments("芥末")
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
"""
