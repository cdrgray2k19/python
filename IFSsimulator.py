import pygame as pg
import sys
from random import randint
import math
vec = pg.math.Vector2



transformations = [
    [[[0, 0],[0, 0.16]],[[0], [0]]],
    [[[0.85, 0.04],[-0.04, 0.85]],[[0], [1.6]]],
    [[[0.2, -0.26],[0.23, 0.22]],[[0], [1.6]]],
    [[[-0.15, 0.28],[0.26, 0.24]],[[0], [0.44]]]
]

def matMult(A, B):
    result = [
        [0],
        [0]
    ]

    for i in range(len(A)):
    
        # iterating by column by B
        for j in range(len(B[0])):
    
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
 
    return result

def matAdd(A, B):
    result = [
        [0],
        [0]
    ]

    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def transform(index, point):
    point = matMult(transformations[index][0], point)
    point = matAdd(transformations[index][1], point)
    return point



WIDTH = 1900*3/4
HEIGHT = 750/9*11
TITLE = 'IFS simulation'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

running = True


point = [[0], [0]]
rotateLeft = [[0,-1], [1,0]]

tIndex = 0
color = (0,255,0)
points = []
screen.fill((255, 255, 255))
while len(points) < 10000000:
    rotatedPoint = matMult(rotateLeft, point)
    points.append([rotatedPoint, color])
    num = randint(0, 100)
    if num <= 1:
        tIndex = 0
        color = (0,255,0)
    elif num <= 86:
        tIndex = 1
        color = (255,255,0)
    elif num <= 93:
        tIndex = 2
        color = (255,0,0)
    else:
        tIndex = 3
        color = (0,0,255)


    point = transform(tIndex, point)
for p, c in points:
    if c == (255,0,0):
        size = 10
    else:
        size = 1
    pg.draw.circle(screen, (0,255,0), vec(p[0][0]*80+WIDTH/1.5, p[1][0]*80/(HEIGHT/WIDTH)+HEIGHT/2), 1)
pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
sys.exit()