import pygame
from pygame import *
import math

size = (1000,600)
screen = pygame.display.set_mode(size)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

groundlevel1 = 500
groundlevel2 = 500

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
        self.vy += self.ay
        self.ypos += self.vy
        
        if self.ypos > self.groundlevel:
            self.ypos = self.groundlevel
            self.vy = 0
            self.jumped = False
                   
    def DrawSquare(self):
        square = pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, 30, 30))
        return square
        
pygame.init()

Run = True
ontwo = False
onone = False

ball1x = 200
ball1y = 500
ball1color = WHITE

ball2x = 800
ball2y = 500
ball2color = BLACK

clock = pygame.time.Clock()

Ball1 = Character(ball1x, ball1y, ball1color, groundlevel1)
Ball2 = Character(ball2x, ball2y, ball2color, groundlevel2)

Ball1.update()
Ball2.update()
    
screen.fill(RED)

Ball1.DrawSquare()
Ball1.DrawSquare()

pygame.display.update()

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
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
    
    Ball1.DrawSquare()
    Ball2.DrawSquare()
    
    pygame.display.update()
    
    clock.tick(60)
