import pygame
import math
import random

xs = 381
ys = 450
xt = xs
yt = ys

dt = 1.0
font = pygame.font.Font(None, 24)

msg = []
msg += ["STOP"]
msg += ["GEAR 1"]
msg += ["GEAR 2"]
msg += ["GEAR 3"]
msg += ["GEAR 4"]
n = len(msg)
gears = []

for i in range(n):
    gears += [font.render(msg[i], 1, (250, 250, 250))]

speedo = []
laps = []

for i in range(1010):
    speedo += [font.render("SPEED " + str(i), 1, (250, 250, 250))]
    laps += [font.render("LAP " + str(i), 1, (250, 250, 250))]
                                
class Sprite:
    def load(self, path, NF):
        self.view = 270
        self.images = []
        self.NF = NF
        self.xc = 437
        self.yc = 800
        self.xf = 437
        self.yf = 800
        self.speed = 0
        self.gear = 1
        self.wobble = 0
        self.lap = 0
        for f in range(NF):
            nv = len(str(f + 1))
            name = path + '/fr_'
            self.images += [pygame.image.load(name + (4 - nv) * '0' + str(f + 1) + '.png')]

    def Draw(self, x, y, screen):
        view = self.view
        if view < 0:
            view = view + 360
        view = view % 360
        screen.blit(self.images[view], (x - 32, y - 32))
        screen.blit(gears[self.gear], (xt, yt))
        screen.blit(speedo[int(self.speed * 100) - int(self.speed * 99)], (xt + 100, yt))
        screen.blit(laps[self.lap], (xt, yt + 50))

    def Update(self):
        theta = self.view / 57.296
        vx = self.speed * math.sin(theta)
        vy = -self.speed * math.cos(theta)
        self.xf = self.xf + vx
        self.yf = self.yf + vy
        self.xc = int(self.xf)
        self.yc = int(self.yf)