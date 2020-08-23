import pygame
from pygame.locals import *

pygame.init()
import car

SIZE = (WIDTH, HEIGHT) = (1280, 1024)
screen = pygame.display.set_mode(SIZE)
screen.fill((0, 192, 0))

clock = pygame.time.Clock()

red = car.Sprite()
red.load('red', 360)

red1 = car.Sprite()
red1.load('red', 360)

red2 = car.Sprite()
red2.load('red', 360)

track = pygame.image.load('track.png')
visible_track = pygame.image.load('track.png')

trk = pygame.Color(0, 192, 0)
barer = pygame.Color(255, 0, 0)
barer1 = pygame.Color(255, 255, 255)
stena = pygame.Color(195, 195, 195)

car.xs = SIZE[0] / 2
car.ys = SIZE[1] / 2

trap = pygame.Rect(844, 1324, 140, 200)

lap = 0
frames = 0

f1 = open('track.txt', 'r').readlines()
f2 = open('track1.txt', 'r').readlines()
f3 = open('track2.txt', 'r').readlines()

running = True
k = 0
while running:
    clock.tick(40)
    frames += 1
    car.frames = frames
    screen.fill((0, 192, 0))
    red.Update()

###################################################################    
# определение пересечения старта-финиша    
###################################################################
    # если машина НЕ в прямоугольнике старта
    #if trap.collidepoint(red.xc, red.yc) == 0:
    #    if inbox == 1: #если она там была
    #        red.lap += 1 # увеличиваем круг
    #        inbox = 0 # сброс флага нахождения в прямоугольнике старта
    #else:
    #    inbox = 1 # если машина В прямоугольнике старта
###################################################################

    screen.blit(visible_track, (0, 0))  # на поверхности screen в координате (car.xs-red.xc,car.ys-red.yc) рисуем поверхность visible_track

    red.Draw(int(f1[k].split()[0]), int(f1[k].split()[1]), screen)  # машина рисуется всегда в одной позиции
    red1.Draw(int(f2[k].split()[0]), int(f2[k].split()[1]), screen)  # машина рисуется всегда в одной позиции
    red2.Draw(int(f3[k].split()[0]), int(f3[k].split()[1]), screen)

    pygame.display.flip()

    red.view = int(f1[k].split()[2])
    red.speed = float(f1[k].split()[3])

    red1.view = int(f2[k].split()[2])
    red1.speed = float(f2[k].split()[3])

    red2.view = int(f3[k].split()[2])
    red2.speed = float(f3[k].split()[3])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k += 1

f1.close()