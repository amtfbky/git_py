#coding=utf-8
import pygame
from pygame.locals import *
import time
import random
class Base(object):
    def __init__(self,x,y,screen,image_name):
        self.x=x
        self.y=y
        self.screen=screen
        self.image=pygame.image.load(image_name).convert()
class BaseBullet(Base):
    def __init__(self,x,y,screen,image_name):
        Base.__init__(self,x,y,screen,image_name)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
class Bullet(BaseBullet):
    def __init__(self,x,y,screen):
          BaseBullet.__init__(self,x+40, y-20, screen,"C:/Users/lenovo/Desktop/feiji/bullet-3.gif")
    def move(self):
            self.y-=10  
    def judge(self):
        if self.y<0:
            return True
        else:   
            return False 
 #谁发射 谁创建       
class EnemyBullet(BaseBullet):
    def __init__(self,x,y,screen):
         BaseBullet.__init__(self,x+25, y+40, screen,"C:/Users/lenovo/Desktop/feiji/bullet1.png")
    def move(self):
            self.y+=5  
    def judge(self):
        if self.y>600:
            return True
        else:   
            return False 
class BasePlane(Base):
    def __init__(self,x,y,screen,image_name):
        Base.__init__(self,x,y,screen,image_name)
        self.bullet_list=[]#存储子弹  
    def display(self):
         #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))
        #存放需要删除的对象信息
        needDelItemList=[]
        for i in self.bullet_list:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bullet_list.remove(i)
        #更新及这架飞机发射出的所有子弹的位置
        #子弹移动了 判断每一颗子弹和子弹的位置
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()    
class HeroPlane(BasePlane):
    def __init__(self,screen):#默认有照片 默认有位置
        BasePlane.__init__(self,200,500,screen,"C:/Users/lenovo/Desktop/feiji/hero.gif")
        self.hit=False #表示是否要爆炸
        self.bomb_list=[]#用来存储爆炸时需要的图片
        self.__create_images()
        self.image_num = 0
     #   用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0#用来记录当前要显示的爆炸效果的图片的序号
    def __create_images(self):
        self.bomb_list.append(pygame.image.load("C:/Users/lenovo/Desktop/feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("C:/Users/lenovo/Desktop/feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("C:/Users/lenovo/Desktop/feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("C:/Users/lenovo/Desktop/feiji/hero_blowup_n4.png"))
    def display(self):
        if self.hit==True:
            self.screen.blit(self.bomb_list[self.image_index],(self.x,self.y))
            self.image_num+=1
            if self.image_num == 5:
                self.image_num=0
                self.image_index+=1
            if self.image_index>3:
                time.sleep(0.1)
                print("failure")
                exit()
        else:
                self.screen.blit(self.image,(self.x, self.y))
            #存放需要删除的对象信息
        needDelItemList=[]
        for i in self.bullet_list:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bullet_list.remove(i)
        #更新及这架飞机发射出的所有子弹的位置
        #子弹移动了 判断每一颗子弹和子弹的位置
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()    
    def bomb(self):
        self.hit = True
    
    def moveLeft(self):
        self.x-=20
    def moveRight(self): 
        self.x+=20
    def moveUp(self):
        self.y-=20
    def moveDown(self):
        self.y+=20
    def fire(self):
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bullet_list.append(newBullet)
class EnemyPlane(BasePlane):
    def __init__(self,screen):
        BasePlane.__init__(self,0,0,screen,"C:/Users/lenovo/Desktop/feiji/enemy0.png")
        self.direction="right"#用来存储飞机默认的显示方向
    def move(self):
        if self.direction=="right":
            self.x+=2
        elif self.direction=="left":
            self.x-=2
        if(self.x>480-50):
            self.direction="left"
        elif(self.x<0):
           self.direction="right"      
    def fire(self):
        random_num=random.randint(1,200)
        if random_num==7 or random_num==20:
            self.bullet_list.append(EnemyBullet(self.x, self.y,self.screen))
def key_control(heroPlane):
     for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key==K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                elif event.key == K_d or event.key==K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                elif event.key == K_w or event.key==K_UP:
                     print('up')
                     heroPlane.moveUp()
                elif event.key ==K_s or event.key==K_DOWN:
                     print('down')
                     heroPlane.moveDown()
                elif event.key == K_SPACE:
                     heroPlane.fire()   
                elif event.key == K_b:
                     print('b')
                     heroPlane.bomb()

        
         
if __name__=="__main__":
    screen=pygame.display.set_mode((480,600),0, 32)
    background=pygame.image.load("C:/Users/lenovo/Desktop/feiji/background.png").convert()
    heroPlane=HeroPlane(screen)
    enemy=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0)) 
        heroPlane.display()
        enemy.display()#让敌机显示
        enemy.move()#调用敌机的move方法
        enemy.fire()#让敌机开火
        pygame.display.update()  
        key_control(heroPlane)
        time.sleep(0.01)
