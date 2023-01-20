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
buttons = []
newplatforms = []
endings = []

global newplats
newplats = False


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

# sets ground level of squares as varibale
groundlevel1 = 500
groundlevel2 = 500

# platform class we used to make all the platforms in the game
class platform:
    def __init__(self, color, xpos, ypos, h, w, listy):
        self.xpos = xpos
        self.color = color
        self.ypos = ypos
        self.w = w
        self.h = h
        listy.append(self)
    
    #draws the platforms
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.w, self.h))

# class that makes the blocks at the end of the game
class ending:
    def __init__(self, color, xpos, ypos, h, w, listy):
        self.xpos = xpos
        self.color = color
        self.ypos = ypos
        self.w = w
        self.h = h
        listy.append(self)
        
    # Draws the ending blocks
    def draw(self):
        endy = pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, self.w, self.h))
        return endy
    
# class that creates the 2 characters and updates there position
class Character:
    def __init__(self, xpos, ypos, color, groundlevel, square):
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.vy = 0
        self.ay = 0.5 
        self.jumped = False
        self.groundlevel = groundlevel
        
    #function that updates the position of the characters
    def update(self):
        # sets onplat to false by default
        onplat = False
        
        # update ypos based on current y velocity
        self.vy += self.ay
        self.ypos += self.vy
        
        # stop moving down if the ypos gets to the ground level
        if self.ypos > self.groundlevel:
            self.ypos = self.groundlevel
            self.vy = 0
            self.jumped = False
            
        # sets variable as true if the character is on one of the platforms
        for plat in platforms:
            if self.xpos < plat.xpos + (plat.w) and self.xpos > plat.xpos - 30:
                if self.ypos + 30 <= plat.ypos + (plat.h / 2) and self.ypos < plat.ypos and self.ypos > plat.ypos - 35:
                    self.groundlevel = plat.ypos - 30
                    onplat = True
                    
        if self.xpos < button1.xpos + (button1.w) and self.xpos > button1.xpos - 30:
            if self.ypos + 30 <= button1.ypos + (button1.h / 2) and self.ypos < button1.ypos and self.ypos > button1.ypos - 35:
                try:
                    buttons.remove(button1)
                    platforms.remove(black1)
                except:
                    pass

        if self.xpos < button2.xpos + (button2.w) and self.xpos > button2.xpos - 30:
            if self.ypos + 30 <= button2.ypos + (button2.h / 2) and self.ypos < button2.ypos and self.ypos > button2.ypos - 35:
                try:
                    buttons.remove(button2)
                    global newplats
                    newplats = True
                except:
                    pass
                
        # subtracts 5 from ground level if not on platform so you fall
        if not onplat:
            self.groundlevel += 5
        
        for plat in platforms:
            if self.xpos < plat.xpos + (plat.w) and self.xpos > plat.xpos - 30:
                if self.ypos <= plat.ypos + plat.h and self.ypos + 30 > plat.ypos + plat.h:
                    self.ypos = plat.ypos + plat.h
                    jumped = False
                   
        if Ball1.ypos + 30 > button1.ypos and Ball1.ypos < button1.ypos + button1.h:
            if Ball1.xpos + 30 > button1.xpos and Ball1.xpos < button1.xpos + button1.w:
                try:
                    buttons.remove(button1)
                    platforms.remove(black1)
                except:
                    pass
                
        if Ball2.ypos + 30 > button2.ypos and Ball2.ypos < button2.ypos + button2.h:
            if Ball2.xpos + 30 > button2.xpos and Ball2.xpos < button2.xpos + button2.w:
                try:
                    buttons.remove(button2)
                    newplats = True
                except:
                    pass

        
    def DrawSquare(self):
        square = pygame.draw.rect(screen, self.color, pygame.Rect(self.xpos, self.ypos, 30, 30))
        return square
        
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

Ball1 = Character(ball1x, ball1y, ball1color, groundlevel1, "square1")
Ball2 = Character(ball2x, ball2y, ball2color, groundlevel2, "square2")

new1 = platform(GREY, 475, 530, 15, 25, newplatforms)
new2 = platform(GREY, 475, 470, 15, 25, newplatforms)
new3 = platform(GREY, 320, 420, 15, 25, newplatforms)
new4 = platform(GREY, 220, 360, 15, 25, newplatforms)

button1 = platform(GREEN, 425, 580, 10, 20, buttons)
button2 = platform(GREEN, 665, 280, 10, 20, buttons)

black1 = platform(DRGREY, 850, 425, 110, 25, platforms)

small1 = platform(GREY, 200, 575, 25, 25, platforms)
small2 = platform(GREY, 350, 525, 75, 25, platforms)
small3 = platform(GREY, 375, 590, 10, 125, platforms)

big1 = platform(GREY, 500, 530, 75, 575, platforms)

big3 = platform(GREY, 0, 530, 70, 100, platforms)

wall1 = platform(GREY, 800, 150, 300, 200, platforms)
wall2 = platform(GREY, 500, 300, 250, 25, platforms)

smallest1 = platform(GREY, 650, 290, 10, 50, platforms)
smallest2 = platform(GREY, 500, 400, 25, 50, platforms)
smallest4 = platform(GREY, 675, 440, 10, 125, platforms)
smallestnew = platform(GREY, 650, 345, 10, 50, platforms)

bump1 = platform(GREY, 600, 495, 35, 25, platforms)
#earlybump = platform(GREY, 475, 505, 25, 25)

floating2 = platform(GREY, 100, 275, 25, 50, platforms)
floating6 = platform(GREY, 125, 175, 25, 100, platforms)
floatingnew = platform(GREY, 300, 300, 50, 20, platforms)
floating1 = platform(GREY, 0, 225, 25, 25, platforms)
floating2 = platform(GREY, 350, 125, 25, 25, platforms)
floating5 = platform(GREY, 550, 125, 25, 40, platforms)

ending1 = ending(DRGREY, 900, 0, 150, 200, endings)

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
    

    if newplats:
        for plat in newplatforms:
            platforms.append(plat)
    
    for plat in platforms:
        plat.draw()
        
    for ending in endings:
        end = ending.draw()
    
    for button in buttons:
        button.draw()
        
    if square1.colliderect(end) and square2.colliderect(end):
        Run = False
    
    
    pygame.display.update()
    
    if Ball1.ypos >= 570 or Ball2.ypos >= 570:
        Run = False
        time.sleep(3)
    
    clock.tick(60)
    
pygame.quit()
