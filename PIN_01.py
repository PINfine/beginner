import pygame

pygame.init()
#创建一个屏幕窗口
screen = pygame.display.set_mode((480,700))
#绘制背景图像
#1.加载图片
bg = pygame.image.load("../image/background.png")
#2.绘制背景图片是屏幕变量进行调用的
screen.blit(bg,(0,0))
#3.更新显示
#update 可以加载完所有的图片后再进行统一调用
pygame.display.update ()
#绘制英雄飞机
hero = pygame.image.load("../image/me1.png")
screen.blit(hero,(150,500))
"""
创建时钟对象，time是个模块，Clock是一个类，tick是一个方法
"""
clock = pygame.time.Clock()
hero_rect=pygame.Rect(150,500,102,126)
pygame.display.update()
while True:
    #每秒执行60次
    clock.tick(60)

    """
    捕获事件event_list = pygame.event.get()
    事件中的get()返回的是一个事件列表
    这一段代码在pygme中是非常固定的
    监听事件
    """
    for event in pygame.event.get():
        #判断事件的类型是否和pygame中的类型一样
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            #直接退出整个事件
            exit()

    hero_rect.y-=5
    if hero_rect.y<=-126:
        hero_rect.y=700
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    pygame.display.update()
    pass
pygame.quit()