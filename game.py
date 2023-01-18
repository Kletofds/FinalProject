import pygame
from pygame import *
import math
import time

platforms = []
endings = []

size = (1000,600)
screen = pygame.display.set_mode(size)

GREEN = (0, 255, 0)
DRGREY = (105, 105, 105)
GREY = (220, 220 ,220)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

groundlevel1 = 500
groundlevel2 = 500

class platform:
    def __init__(self, color, xpos, ypos, h, w):
        self.xpos = xpos
        self.color = color
        self.ypos = ypos
        self.w = w
        self.h = h
        platforms.append(self)
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.w, self.h))

class end:
    def __init__(self, color, xpos, ypos, h, w):
        self.xpos = xpos
        self.color = color
        self.ypos = ypos
        self.w = w
        self.h = h
        endings.append(self)
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.w, self.h))

class Character:
    def __init__(self, xpos, ypos, color, groundlevel):
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.vy = 0
        self.ay = 0.5 
        self.jumped = False
        self.groundlevel = groundlevel
        
    def update(self):
        onplat = False
        
        self.vy += self.ay
        self.ypos += self.vy
        
        if self.ypos > self.groundlevel:
            self.ypos = self.groundlevel
            self.vy = 0
            self.jumped = False
            
        for plat in platforms:
            if self.xpos <= plat.xpos + (plat.w) and self.xpos >= plat.xpos:
                if self.ypos + 30 <= plat.ypos + (plat.h / 2) and self.ypos < plat.ypos:
                    self.groundlevel = plat.ypos - 30
                    onplat = True
                
        if not onplat:
            self.groundlevel += 5
                   
    def DrawSquare(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, 30, 30))

        
pygame.init()

Run = True
ontwo = False
onone = False
oneonplat = True

ball1x = 200
ball1y = 500
ball1color = WHITE

ball2x = 900
ball2y = 500
ball2color = BLACK

clock = pygame.time.Clock()

Ball1 = Character(ball1x, ball1y, ball1color, groundlevel1)
Ball2 = Character(ball2x, ball2y, ball2color, groundlevel2)

#platform

black1 = platform(DRGREY, 850, 425, 110, 25)

white1 = platform(DRGREY, 500, 450, 80, 25)

small1 = platform(GREY, 250, 575, 25, 25)
small2 = platform(GREY, 350, 550, 50, 25)

big1 = platform(GREY, 425, 530, 75, 575)
big2 = platform(GREY, 600, 530, 75, 400)
big3 = platform(GREY, 0, 530, 70, 300)

wall1 = platform(GREY, 800, 150, 300, 100)
wall2 = platform(GREY, 500, 300, 175, 25)

smallest1 = platform(GREY, 650, 275, 25, 50)
smallest2 = platform(GREY, 500, 450, 25, 50)
smallest4 = platform(GREY, 675, 440, 10, 125)

bump1 = platform(GREY, 600, 495, 35, 25)

floating1 = platform(GREY, 200, 150, 50, 1000)
floating2 = platform(GREY, 100, 275, 50, 100)
floating6 = platform(GREY, 125, 175, 25, 100)

ending = end(DRGREY, 900, 0, 150, 200)

Ball1.update()
Ball2.update()
    
screen.fill(RED)

square1 = Ball1.DrawSquare()
square2 = Ball2.DrawSquare()

pygame.display.update()

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            
    keys = pygame.key.get_pressed()
    oneonplat= False
    
    if keys[pygame.K_d]:
        Ball1.xpos += 5
           
    if keys[pygame.K_a]:
        Ball1.xpos -= 5
    
    if keys[pygame.K_RIGHT]:
        Ball2.xpos += 5
        
    if keys[pygame.K_LEFT]:
        Ball2.xpos -= 5
        
    if keys[pygame.K_w] and not Ball1.jumped:
        Ball1.vy = -8
        Ball1.jumped = True
        
    if keys[pygame.K_UP] and not Ball2.jumped:
        Ball2.vy = -8
        Ball2.jumped = True    
            
    if Ball1.xpos < 30:
        Ball1.xpos = 30
        
    if Ball1.xpos > 970:
        Ball1.xpos = 970
        
    if Ball2.xpos < 30:
        Ball2.xpos = 30
        
    if Ball2.xpos > 970:
        Ball2.xpos = 970
        
    if Ball1.ypos < Ball2.ypos + 30 and Ball1.ypos > Ball2.ypos - 30 or Ball2.ypos < Ball1.ypos + 30 and Ball2.ypos > Ball1.ypos - 30:
        if Ball1.xpos >= Ball2.xpos - 30 and Ball1.xpos < Ball2.xpos and keys[pygame.K_d]:
            Ball1.xpos = Ball2.xpos - 30  
        if Ball1.xpos <= Ball2.xpos + 30 and Ball1.xpos > Ball2.xpos and keys[pygame.K_a]:
            Ball1.xpos = Ball2.xpos + 30       
        if Ball2.xpos <= Ball1.xpos + 30 and Ball2.xpos > Ball1.xpos and keys[pygame.K_LEFT]:
            Ball2.xpos = Ball1.xpos + 30   
        if Ball2.xpos >= Ball1.xpos - 30 and Ball2.xpos < Ball1.xpos and keys[pygame.K_RIGHT]:
            Ball2.xpos = Ball1.xpos - 30
                
    if Ball1.xpos < Ball2.xpos + 30 and Ball1.xpos > Ball2.xpos - 30 or Ball2.xpos < Ball1.xpos + 30 and Ball2.xpos > Ball1.xpos - 30:
        if Ball1.ypos >= Ball2.ypos - 30 and Ball1.ypos < Ball2.ypos:
            Ball1.ypos = Ball2.ypos - 30
            Ball1.groundlevel = Ball2.ypos - 30
            ontwo = True
            
        if Ball2.ypos >= Ball1.ypos - 30 and Ball2.ypos < Ball1.ypos:
            Ball2.ypos = Ball1.ypos - 30
            Ball2.groundlevel = Ball1.ypos - 30
            onone = True
            
    if ontwo:
        if Ball1.xpos > Ball2.xpos + 30 or Ball1.xpos < Ball2.xpos - 30:
            ontwo = False
            Ball1.groundlevel = Ball2.groundlevel
            
    if onone:
        if Ball2.xpos > Ball1.xpos + 30 or Ball2.xpos < Ball1.xpos - 30:
            onone = False
            Ball2.groundlevel = Ball1.groundlevel
            

            
    Ball1.update()
    Ball2.update()
        
    screen.fill(RED)
    
    square1 = Ball1.DrawSquare()
    square2 = Ball2.DrawSquare()
    
    for plat in platforms:
        plat.draw()
    for ends in endings:
        ends.draw()
    pygame.display.update()
    
    if Ball1.ypos >= 570 or Ball2.ypos >= 570:
        Run = False
        time.sleep(3)
    
    clock.tick(60)
    
pygame.quit()
