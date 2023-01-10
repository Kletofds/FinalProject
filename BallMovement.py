import pygame
from pygame import *
import math

size = (1000,600)
screen = pygame.display.set_mode(size)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class Ball:
    def __init__(self, xpos, ypos, color):
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.vx = 0
        self.vy = 0
        self.ay = 0.5 
        self.ax = 0
        self.jumped = False
        
    def update(self):
        self.vy += self.ay
        self.ypos += self.vy
        
        self.vx += self.ax
        self.xpos += self.vx
        
        if self.ypos > 570:
            self.ypos = 570
            self.vy = 0
            self.jumped = False
                   
    def DrawBall(self):
        pygame.draw.circle(screen, (self.color), (self.xpos, self.ypos), 30, 0)
        
def CheckCollision(b1, b2):
    dist = math.sqrt((b1.xpos - b2.xpos)**2 + (b1.ypos - b2.ypos)**2)
        
    if dist < 65:     
        return True
    else:
        return False
        
pygame.init()

Run = True

ball1x = 200
ball1y = 500
ball1color = WHITE

ball2x = 800
ball2y = 500
ball2color = BLACK

clock = pygame.time.Clock()

Ball1 = Ball(ball1x, ball1y, ball1color)
Ball2 = Ball(ball2x, ball2y, ball2color)

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
    CollideCheck = CheckCollision(Ball1, Ball2)
    
    if keys[pygame.K_d]:
        if CollideCheck and Ball1.xpos < Ball2.xpos:
            Ball1.xpos = Ball2.xpos - 60
        else:
            Ball1.xpos += 5
        
    if keys[pygame.K_a]:
        if CollideCheck and Ball1.xpos > Ball2.xpos:
            Ball1xpos = Ball2.xpos + 60
        else:
            Ball1.xpos -= 5
    
    if keys[pygame.K_RIGHT]:
        if CollideCheck and Ball1.xpos > Ball2.xpos:
            Ball2.xpos = Ball1.xpos - 60
        else:
            Ball2.xpos += 5
        
    if keys[pygame.K_LEFT]:
        if CollideCheck and Ball1.xpos < Ball2.xpos:
            Ball2.xpos = Ball1.xpos + 60
        else:
            Ball2.xpos -= 5
        
    if keys[pygame.K_w] and not Ball1.jumped:
        Ball1.vy = -10
        Ball1.jumped = True
        
    if keys[pygame.K_UP] and not Ball2.jumped:
        Ball2.vy = -10
        Ball2.jumped = True    
            
    if Ball1.xpos < 30:
        Ball1.xpos = 30
        
    if Ball1.xpos > 970:
        Ball1.xpos = 970
        
    if Ball2.xpos < 30:
        Ball2.xpos = 30
        
    if Ball2.xpos > 970:
        Ball2.xpos = 970 
               
    Ball1.update()
    Ball2.update()
        
    screen.fill(RED)
    
    Ball1.DrawBall()
    Ball2.DrawBall()
    
    pygame.display.update()
    
    clock.tick(60)
    
    
    