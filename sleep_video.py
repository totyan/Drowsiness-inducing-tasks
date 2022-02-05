import time
import pygame
import math
import threading

def roll():
    t = 0
    #円の半径
    r = 200
    while (1):
        pygame.display.update()# 画面更新
        #pygame.time.wait(1)# 更新時間間隔
        surface.fill((0, 20, 0, 0))# 画面の背景色
        surface.blit(image, rect)
        rect.center = (wh/2, wh/2)
        x = r * math.cos(math.radians(2*t))
        y = r * math.sin(math.radians(2*t))
        rect.move_ip(x,y)
        t=t+1.5

pygame.init()
pygame.display.set_caption('')
size = pygame.display.Info()
#ww = int(size.current_w/2)
wh = int(size.current_h/2)
surface = pygame.display.set_mode((wh, wh)) 


image = pygame.image.load("picture_path").convert_alpha()
rect = image.get_rect()

t1 = threading.Thread(target=roll)
t1.setDaemon(True)
t1.start()
time.sleep(900)








