"""primes = [1] * 10000001
primes[0] = 0
primes[1] = 0
primeFile = open("primeNums.txt", "w")
for n in range(2, len(primes)):
    if primes[n] == 0:
        continue
    primeFile.write(str(n) + "\n")
    for i in range(n*2, len(primes), n):
        primes[i] = 0"""

import pygame as pg
import sys
from random import randint
import math
vec = pg.math.Vector2

WIDTH = 1900*3/4
HEIGHT = 750/9*11
TITLE = 'IFS simulation'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

running = True

col = (0, 255, 0)
with open("primeNums.txt", "r") as f:
    primes = list(map(lambda x: int(x), f.readlines()))

screen.fill((255, 255, 255))
theta = -0.01
for i in range(0, len(primes)):
    p = primes[i]
    #theta += 0.01
    x = math.cos(p) * p / 20000
    y = math.sin(p) * p / 20000
    x += WIDTH/2
    y += HEIGHT/2
    pg.draw.circle(screen, col, vec(x,y), 1)
pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
sys.exit()