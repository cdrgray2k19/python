import pygame as pg
import sys
from random import randint
import math
vec = pg.math.Vector2

WIDTH = 1400
HEIGHT = 800
TITLE = 'bézier curves'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

p1 = vec(randint(0, 1400), randint(0, 800))
p2 = vec(randint(0, 1400), randint(0, 800))
p3 = vec(randint(0, 1400), randint(0, 800))
p4 = vec(randint(0, 1400), randint(0, 800))


points = [p1, p2, p3, p4]

print(points)

running = True
t = 0
speed = 0.005

cubicPoints = []
while running:
    screen.fill((255, 255, 255))
    

    t += speed
    
    if t > 1:
        
        p1 = vec(randint(0, 1400), randint(0, 800))
        p2 = vec(randint(0, 1400), randint(0, 800))
        p3 = vec(randint(0, 1400), randint(0, 800))
        p4 = vec(randint(0, 1400), randint(0, 800))


        points = [p1, p2, p3, p4]

        print(points)
        
        t = 0
        cubicPoints = []
    
    '''
    point = p1 * (math.pow(1-t, 3)) + p2 * (3 * t * (math.pow(1-1, 2))) + p3 * (3 * (1-t) * math.pow(t, 2)) + p4 * (math.pow(t, 3))
    cubicPoints.append(point)
    size = 1
    for i in range(0, len(cubicPoints) - 1):
        if i == len(cubicPoints) - 1:
            size = 4
        pg.draw.circle(screen, (255, 0, 255), cubicPoints[i], size)

    '''

    for i in range(0, len(points) - 1):
        pg.draw.line(screen, (0, 0, 255), points[i], points[i+1], 3)
    for i in range(0, len(points)):
        pg.draw.circle(screen, (0,255,0), points[i], 4)
    
    newPoints = []
    quadPoints = []
    for i in range(0, len(points) - 1):
        point = ((1-t) * points[i]) + (t*points[i+1])
        newPoints.append(point)
        pg.draw.circle(screen, (255, 0, 0), point, 4)
    
    for i in range(0, len(newPoints) - 1):
        pg.draw.line(screen, (0, 0, 255), newPoints[i], newPoints[i+1], 3)
        point = ((1-t) * newPoints[i]) + (t*newPoints[i+1])
        pg.draw.circle(screen, (255, 0, 0), point, 4)
        quadPoints.append(point)

    for i in range(0, len(quadPoints) - 1):
        pg.draw.line(screen, (0, 0, 255), quadPoints[i], quadPoints[i+1], 3)
        point = ((1-t) * quadPoints[i]) + (t*quadPoints[i+1])
        pg.draw.circle(screen, (255, 0, 0), point, 4)
        cubicPoints.append(point)

    size = 1
    for i in range(0, len(cubicPoints) - 1):
        if i == len(cubicPoints) - 1:
            size = 4
        pg.draw.circle(screen, (255, 0, 255), cubicPoints[i], size)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()


pg.quit()
sys.exit()