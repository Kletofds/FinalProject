##################################
#        Twogether Slide         #
#         01, 07, 2023           #
#      B1GM6N and Kletofds       #
##################################

# import modules
import pygame
from pygame import *
import math
import time

#lists for platforms and the ending 
platforms = []
endings = []

# prepares screen size
size = (1000,600)
screen = pygame.display.set_mode(size)
# RGB colors
GREEN = (0, 255, 0)
DRGREY = (105, 105, 105)
GREY = (220, 220 ,220)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

groundlevel1 = 500
groundlevel2 = 500

# platform class we used to make all the platforms in the game
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
            if self.xpos < plat.xpos + (plat.w) and self.xpos > plat.xpos - 30:
                if self.ypos + 30 <= plat.ypos + (plat.h / 2) and self.ypos < plat.ypos and self.ypos > plat.ypos - 35:
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

ball1x = 50
ball1y = 500
ball1color = WHITE

ball2x = 900
ball2y = 500
ball2color = BLACK

clock = pygame.time.Clock()

Ball1 = Character(ball1x, ball1y, ball1color, groundlevel1)
Ball2 = Character(ball2x, ball2y, ball2color, groundlevel2)



black1 = platform(DRGREY, 850, 425, 110, 25)

small1 = platform(GREY, 200, 575, 25, 25)
small2 = platform(GREY, 350, 525, 75, 25)
small3 = platform(GREY, 375, 590, 10, 125)

big1 = platform(GREY, 500, 530, 75, 575)

big3 = platform(GREY, 0, 530, 70, 100)

wall1 = platform(GREY, 800, 150, 300, 200)
wall2 = platform(GREY, 500, 300, 250, 25)

smallest1 = platform(GREY, 650, 290, 10, 50)
smallest2 = platform(GREY, 500, 400, 25, 50)
smallest4 = platform(GREY, 675, 440, 10, 125)
smallestnew = platform(GREY, 650, 345, 10, 50)

bump1 = platform(GREY, 600, 495, 35, 25)
#earlybump = platform(GREY, 475, 505, 25, 25)

floating2 = platform(GREY, 100, 275, 25, 50)
floating6 = platform(GREY, 125, 175, 25, 100)
floatingnew = platform(GREY, 300, 300, 50, 20)
floating1 = platform(GREY, 0, 225, 25, 25)
floating2 = platform(GREY, 350, 125, 25, 25)
floating5 = platform(GREY, 550, 125, 25, 40)

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
            
    if Ball1.xpos < 0:
        Ball1.xpos = 0
        
    if Ball1.xpos > 970:
        Ball1.xpos = 970
        
    if Ball2.xpos < 0:
        Ball2.xpos = 0
        
    if Ball2.xpos > 970:
        Ball2.xpos = 970
    
    for plat in platforms:
        if Ball1.ypos + 30 > plat.ypos and Ball1.ypos < plat.ypos + plat.h:
            if keys[pygame.K_d] and Ball1.xpos + 30 >= plat.xpos and Ball1.xpos < plat.xpos:
                Ball1.xpos = plat.xpos - 30
            if keys[pygame.K_a] and Ball1.xpos <= plat.xpos + plat.w and Ball1.xpos + 35 > plat.xpos + plat.w:
                Ball1.xpos = plat.xpos + plat.w

        if Ball2.ypos + 30 > plat.ypos and Ball2.ypos < plat.ypos + plat.h:
            if keys[pygame.K_RIGHT] and Ball2.xpos + 30 >= plat.xpos and Ball2.xpos < plat.xpos:
                Ball2.xpos = plat.xpos - 30
            if keys[pygame.K_LEFT] and Ball2.xpos <= plat.xpos + plat.w and Ball2.xpos + 35 > plat.xpos + plat.w:
                Ball2.xpos = plat.xpos + plat.w    
    
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