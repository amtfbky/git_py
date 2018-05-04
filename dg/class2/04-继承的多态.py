class Dog(object):
    def print_self(self):
        print("大家好，我是xxx，希望以后大家多多关照...")

class Xiaotq(Dog):
    def print_self(sefl):
        print("hello everybody，我是你们的老大，我是xxx")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2) # 在执行的一刹那才决定调谁，这就是多态
# Python既是面向过程，又是面向对象
# 封装继承多态，三要素
"""理解多态：
    游戏触摸版:创建角色时，调用角色的方法一样，但选择角色的对象不同，这就是多态
    安卓主题不同，按钮的颜色随着主题变化而变化，但按钮的功能一样"""

