class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num
t = Test()
#t.__num = 200
#print(t.__num)

print(t.getNum())
t.setNum(50)
print(t.getNum())
