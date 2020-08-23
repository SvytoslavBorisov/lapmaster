import pygame
from pygame.locals import *
import math


#points = [[300, 610],
#                      [1270,430],
#                      [1380,2380],
#                      [1900,2460],
#                      [1970,1700],
#                      [2550,1680],
#                      [2560,3150],
#                      [500, 3300]]

pygame.init()

points = [[156, 312],
          [314, 183],
          [430, 309],
          [400, 730],
          [585, 743],
          [590, 318],
          [665, 240],
          [1325, 243],
          [1366, 311],
          [1377, 479],
          [1294, 552],
          [878, 565],
          [785, 644],
          [872, 738],
          [1292, 745],
          [1362, 814],
          [1371, 1283],
          [1266, 1372],
          [1136, 1271],
          [1126, 1040],
          [979, 948],
          [816, 1014],
          [795, 1292],
          [725, 1392],
          [617, 1334],
          [215, 930],
          [205, 641]]

num = len(points)

class Car:
    def __init__(self, sprite, name, coords=(0, 0), speed=2, angle=0, n=0):
        self.x = coords[0] * 2
        self.y = coords[1] * 2
        self.n = n
        sprite.set_colorkey((255, 255, 255))
        self.sprite = sprite
        self.angle = 0
        self.speed = 2
        self.inbox = 1
        self.lap = 0
        self.name = name
        self.Name = font.render(name, 1, (250, 250, 250))
        self.time = [0]
        self.globN = 0

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def findTarget(self):
        tx = points[self.n][0] * 2
        ty = points[self.n][1] * 2
        beta = self.angle - math.atan2(tx - self.x, -ty + self.y)
        ddd = math.sin(beta)
        if abs(ddd) < 0.08:
            ddd = 0
        if ddd < 0:
            self.angle += 0.004 * self.speed
        else:
            self.angle -= 0.004 * self.speed
        if (self.x - tx) * (self.x - tx) + (self.y - ty) * (self.y - ty) < 200 * 25:
            self.n = (self.n + 1) % num
            self.globN += 1


SIZE = (WIDTH, HEIGHT) = (1024, 1024)

font = pygame.font.Font(None, 24)
screen = pygame.display.set_mode(SIZE)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()

names = ['МАКС ФЕРСТАППЕН', 'ДАНИИЛ КВЯТ', 'ЛЬЮИС ХЭМИЛТОН', 'СЕБАСТЬЯН ФЕТТЕЛЬ', 'ПЬЕР ГАСЛИ']
sprites = [pygame.image.load('carRB.png').convert(),
           pygame.image.load('carReno.png').convert(),
           pygame.image.load('carMers.png').convert(),
           pygame.image.load('carFerrari.png').convert(),
           pygame.image.load('carRaceP.png').convert()]

coords = [(175, 545),
          (230, 545),
          (230, 620),
          (175, 620),
          (230, 690)]

sBackground = pygame.image.load('la_mash.png')
sBackground = pygame.transform.scale(sBackground, (sBackground.get_width() * 2, sBackground.get_height() * 2))

R = 22

N = 5
car = [Car(sprites[i], names[i], coords=coords[i]) for i in range(5)]
carTemp = car

for i in range(N):
    car[i].speed = 15 + i * 0.1

pygame.display.flip()

trap = pygame.Rect(220, 1756, 418, 1820)

offsetX = 0
offsetY = 0
view = 1

running = True
while running:

    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        view = (view + 1) % N
    if keys[K_LEFT]:
        view = (view - 1) % N

    for i in range(N):
        if trap.collidepoint(car[i].x, car[i].y) == 0:
            if car[i].inbox == 1:
                car[i].lap += 1
                car[i].inbox = 0
                car[i].time.append(0)
        else:
            car[i].inbox = 1

    for i in range(N):
        car[i].move()

    for i in range(N):
        car[i].findTarget()

    for i in range(N):
        for j in range(N):
            dx = 0
            dy = 0
            while dx * dx + dy * dy < 4 * R * R:
                car[i].x += dx / 10.0
                car[i].y += dy / 10.0
                car[j].x -= dx / 10.0
                car[j].y -= dy / 10.0
                dx = car[i].x - car[j].x
                dy = car[i].y - car[j].y
                if not dx and not dy:
                    break

    screen.fill((0, 0, 0))

    if car[view - 1].x > 320:
        offsetX = car[view - 1].x - 320
    if car[view - 1].y > 240:
        offsetY = car[view - 1].y - 240

    screen.blit(sBackground, (-offsetX, -offsetY, 0, 0))

    colors = [pygame.Color(255, 0, 0),
              pygame.Color(0, 255, 0),
              pygame.Color(0, 0, 255),
              pygame.Color(255, 255, 0),
              pygame.Color(255, 255, 255)]

    for i in range(N):
        sCarTemp = pygame.transform.rotate(car[i].sprite, int(-car[i].angle * 180 / 3.141593))
        car[i].time[-1] += 1
        screen.blit(sCarTemp, (car[i].x - offsetX, car[i].y - offsetY))

    carTemp = sorted(carTemp, key=lambda x: x.globN, reverse=True)
    for i in range(N):
        screen.blit(font.render(carTemp[i].name + ' ' + str(i + 1), 1, (250, 250, 250)), (0, i * 20))

    pygame.display.flip()

