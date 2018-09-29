import random
"""
导入模块的顺序 官方 第三方 模块程序
"""
import pygame


"""飞机大战游戏精灵"""
SCREEN_RECT = pygame.Rect(0,0,480,700)
#USEREVENT 是pygame提供的用户常量，便于认识
CREATE_ARMY_EVENT = pygame.USEREVENT
CREATE_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        #调用父类的初始化方法
        super().__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class BackGround(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt=False):
        super().__init__("./image/background.png")
        #这个是传递过来的参数
        if is_alt == True:
            self.rect.y = self.rect.height
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #调用父类方法，创建敌机，同时增加敌机图片
        super().__init__("./image/enemy1.png")
        self.speed = random.randint(1,3)
        self.rect.x = random.randint(0,423)
        self.rect.y = -43

    def update(self):
       super().update()

       if self.rect.y >= SCREEN_RECT.height:
           #kill()将精灵从所有精灵组中删除并自动销毁
           self.kill()
    #当有对象被删除时会自己调用这个函数
    def __del__(self):
        pass

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./image/me1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建精灵组
        self.bullet_ground = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= SCREEN_RECT.width - 100:
            self.rect.x -= 2
            print("英雄到达边界")
        elif self.rect.x <= 0:
            self.rect.x += 2
            print("英雄到达边界")
        else:
            pass
    def fire(self):
        for i in (0,1,2):
            #创建子弹精灵
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - int(i)*20
            bullet.rect.centerx = self.rect.centerx

            #添加的精灵组。只有是精灵组变量才可以调用add函数
            self.bullet_ground.add(bullet)

class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./image/bullet2.png",-2)
    def update(self):
        #调用父类的方法
        super().update()
        #删除精灵
        if self.rect.y < 0:
            self.kill()
    def __del__(self):
        pass