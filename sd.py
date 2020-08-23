import pygame
import math
import sys


class Sprite:
    def load(self, path):
        self.angle = 0
        self.images = []
        self.CoordX = 437
        self.CoordY = 800
        self.coords = (self.CoordX, self.CoordY) = (0, 0)
        self.speed = 5
        self.TOCKA = 1
        self.pos = pygame.math.Vector2((self.CoordX, self.CoordY))
        f = open('MainTrack1.txt', 'r')
        f.close()
        for f in range(360):
            nv = len(str(f + 1))
            name = path + '/fr_'
            self.images += [pygame.image.load(name + (4 - nv) * '0' + str(f + 1) + '.png')]

    def Draw(self, x, y, screen):
        image = pygame.transform.rotate(self.images[0], math.degrees(self.angle))
        screen.blit(image, (x - 32, y - 32))

    def follow(self, coordTo):
        beta = self.angle - math.atan2(coordTo[0] - self.CoordX, -coordTo[1] + self.CoordY)
        if math.sin(beta) < 0:
            self.angle += 0.005 * self.speed
        else:
            self.angle -= 0.005 * self.speed

        self.CoordX += math.sin(self.angle) * self.speed
        self.CoordY -= math.cos(self.angle) * self.speed
        return True


SIZE = (WIDTH, HEIGHT) = (1280, 1024)

pygame.init()
screen = pygame.display.set_mode(SIZE)
screen.fill((0, 192, 0))

clock = pygame.time.Clock()

red = Sprite()
red.load('red')

track = pygame.image.load('track.png')
visible_track = pygame.image.load('track.png')

trk = pygame.Color(0, 192, 0)
barer = pygame.Color(255, 0, 0)
barer1 = pygame.Color(255, 255, 255)
stena = pygame.Color(195, 195, 195)

f = open('MainTrack1.txt', 'r')
data = f.readlines()

red.CoordX = int(data[0].split()[0])
red.CoordY = int(data[0].split()[1])

x1 = int(data[red.TOCKA].split()[0])
y1 = int(data[red.TOCKA].split()[1])

running = True
k = 0
while running:
    clock.tick(50)
    screen.fill((0, 192, 0))
    if red.follow((x1, y1)):
        red.TOCKA += 1
        x1 = int(data[red.TOCKA % len(data)].split()[0])
        y1 = int(data[red.TOCKA % len(data)].split()[1])

    screen.blit(visible_track, (0, 0))  # на поверхности screen в координате (car.xs-red.xc,car.ys-red.yc) рисуем поверхность visible_track
    red.Draw(red.CoordX, red.CoordY, screen)  # машина рисуется всегда в одной позиции
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

f.close()