import pygame
from plane_sprites import *

class PlaneGame():
    """飞机大战主程序"""
    def __init__(self):
        print("游戏初始化")
        #display是一个模块
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        #调用方法创建精灵和精灵组
        self.__create_sprites()

        #设置定时器事件，创建敌机,1s中触发一次事件，并用事件监听来捕获定时器
        #第一个参数便是set_timer函数的常量,而且这个事件常量是一盒int
        pygame.time.set_timer(CREATE_ARMY_EVENT,1000)
        pygame.time.set_timer(CREATE_FIRE_EVENT,500)

    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        #添加到精灵组
        self.back_ground = pygame.sprite.Group(bg1,bg2)
        #创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        #创建英雄精灵
        self.hero = Hero()
        #创建英雄精灵组
        self.hero_ground = pygame.sprite.Group(self.hero)



    def start_game(self):
        print("游戏开始")
        while True:
            #设置游戏刷新帧率
            self.clock.tick(60)
            #事件监听
            self.__event_handler()
            #检测碰撞
            self.__check_collide()
            #更新绘制精灵组
            self.__update_sprties()
            #更新显示
            pygame.display.update()
            pass
            #这个函数是两个精灵组中所有精灵的碰撞
            pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_ground,True,True)
            #某个精灵和制定精灵组的碰撞检测，精灵组中的精灵会自动删除，并且返回精灵组中碰撞的精灵的列表
            enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
            """
            这样子是一个非常好的方法，用len函数来判断列表中是否有返回值
            """
            if len(enemies) > 0:
                self.hero.kill()
                #结束游戏
                pygame.quit()
                exit()

    def __event_handler(self):
        #返回的是一个事件类型的列表
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #静态方法的调用
                PlaneGame.__game_over()
            elif event.type == CREATE_ARMY_EVENT:
                #创建敌机精灵
                enemy = Enemy()
                #添加的精灵组里
                self.enemy_group.add(enemy)

            elif event.type == CREATE_FIRE_EVENT:
                self.hero.fire()
            #返回所有按键的元组
            key_pressed = pygame.key.get_pressed()
            #通键盘常量里应该每个键对应一个数判断键是否按下，按下对应的值是 1，否则是0
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2


    def __check_collide(self):
        pass
    def __update_sprties(self):
        #让组中所有的精灵调用自己的update
        self.back_ground.update()
        #在屏幕重新绘制更新后的精灵
        self.back_ground.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_ground.update()
        self.hero_ground.draw(self.screen)
        self.hero.bullet_ground.update()
        self.hero.bullet_ground.draw(self.screen)
    #静态方法
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

#将自己当成模块进行导入。注释：每一个单独的.py文件都可以当成模块进行导入
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()