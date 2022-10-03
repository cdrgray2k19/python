import pygame as pg
import sys
from random import randint
import math
vec = pg.math.Vector2


WIDTH = 1900
HEIGHT = 1025
TITLE = 'triangulation'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

pg.font.init()
my_font = pg.font.SysFont('freesansbold.ttf', 30)

running = True

epi = vec(randint(0, WIDTH), randint(0, HEIGHT))
p1 = vec(650, 350)
p2 = vec(1250, 350)
p3 = vec(950, 700)

p1Dist = math.sqrt((p1.x-epi.x)**2 + (p1.y-epi.y)**2)
p2Dist = math.sqrt((p2.x-epi.x)**2 + (p2.y-epi.y)**2)
p3Dist = math.sqrt((p3.x-epi.x)**2 + (p3.y-epi.y)**2)

while running:
    screen.fill((255, 255, 255))

    pg.draw.circle(screen, (0,0,255), p1, 4)
    pg.draw.circle(screen, (0,0,255), p2, 4)
    pg.draw.circle(screen, (0,0,255), p3, 4)

    pg.draw.circle(screen, (0,255,0), epi, 10)



    pg.draw.circle(screen, (255,0,0), p1, p1Dist, width = 1)
    pg.draw.circle(screen, (255,0,0), p2, p2Dist, width = 1)
    pg.draw.circle(screen, (255,0,0), p3, p3Dist, width = 1)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                epi = vec(randint(0, WIDTH), randint(0, HEIGHT))
                p1Dist = math.sqrt((p1.x-epi.x)**2 + (p1.y-epi.y)**2)
                p2Dist = math.sqrt((p2.x-epi.x)**2 + (p2.y-epi.y)**2)
                p3Dist = math.sqrt((p3.x-epi.x)**2 + (p3.y-epi.y)**2)
            elif event.key == pg.K_q:
                running = False
    

    text_surface = my_font.render(str(int(p1Dist))+'px', False, (0, 0, 0))
    screen.blit(text_surface, (p1.x, p1.y-20))
    text_surface = my_font.render(str(int(p2Dist))+'px', False, (0, 0, 0))
    screen.blit(text_surface, (p2.x, p2.y-20))
    text_surface = my_font.render(str(int(p3Dist))+'px', False, (0, 0, 0))
    screen.blit(text_surface, (p3.x, p3.y-20))
    pg.display.update()


pg.quit()
sys.exit()