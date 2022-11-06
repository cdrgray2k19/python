import pygame as pg
import sys
from random import randint
import math


WIDTH = 1400
HEIGHT = 800
TITLE = 'bézier curves'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    
    
    screen.fill((255, 255, 255))
    pg.display.update()


pg.quit()
sys.exit()