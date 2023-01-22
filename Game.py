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

# RGB colors
GREEN = (0, 255, 0)
DRGREY = (105, 105, 105)
GREY = (220, 220 ,220)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
        
# Function that replaces score on leaderboard with new time
def replaceline(list_num):
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    lines[list_num] = f"{name}: {endtime}\n"
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)
            
# Function that moves leaderboard down so it adds new score instead of replacing old one
def movedown(list_num):
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    lines[list_num] = f"\n{lines[list_num]}"
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)
            
# Function that deletes extra line after moving down
def delete_extra_line():
    with open ('Leaderboard.txt') as file:
        lines = file.readlines()
        
    del lines[10]
    
    with open('Leaderboard.txt', 'w') as file:
        for line in lines:
            file.write(line)
        
pygame.init()
Run = True
clock = pygame.time.Clock()

print("What is your name?")
name = input("> ")

# prepares screen size
size = (1000,600)
screen = pygame.display.set_mode(size)

while Run:
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

    class Button:
        def __init__(self, rectypos, rectxpos, rect_width, rect_height, text, textx, texty):
            self.rectypos = rectypos
            self.rectxpos = rectxpos
            self.rect_width = rect_width
            self.rect_height = rect_height
            self.text = text
            self.textx = textx
            self.texty = texty
            
        def DrawButton(self):
            button_rect = pygame.Rect(self.rectypos, self.rectxpos, self.rect_width, self.rect_height)
            
            pygame.draw.rect(screen, BLACK, button_rect)
            
            button_text = buttonfont.render(self.text, True, WHITE)
            
            screen.blit(button_text, (self.textx, self.texty))
        
    
    buttonfont = pygame.font.Font(None, 40)
    titlefont = pygame.font.Font(None, 100)
    leaderboardfont = pygame.font.Font(None, 40)

    Game = False
    Screen = True
    Leaderboard = False
    Complete = False

    while Screen and Run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            
        screen.fill(WHITE)
        
        button1 = Button(400, 300, 200, 50, "Start Game", 426, 312)
        button2 = Button(400, 360, 200, 50, "Leaderboard", 415, 372)
        button3 = Button(400, 420, 200, 50, "Quit", 465, 432)

        button1.DrawButton()
        button2.DrawButton()
        button3.DrawButton()
        
        title_text = titlefont.render("Two-gether Roll", True, BLUE)
        screen.blit(title_text, (245, 100))
        
        pygame.display.update()

        if pygame.mouse.get_pressed()[0] == 1:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if 400 <= mouse_x <= 600 and 300 <= mouse_y <= 350:
                Screen = False
                Game = True
                
            if 400 <= mouse_x <= 600 and 360 <= mouse_y <= 410:
                Screen = False
                Leaderboard = True
                
            if 400 <= mouse_x <= 600 and 420 <= mouse_y <= 470:
                Screen = False
                Run = False
                
    if Game and Run:
        ontwo = False
        onone = False
        oneonplat = True
        
        ball1x = 50
        ball1y = 500
        ball1color = WHITE

        ball2x = 900
        ball2y = 500
        ball2color = BLACK
        
        # sets ground level of squares as varibale
        groundlevel1 = 500
        groundlevel2 = 500
        
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

        starttime = time.time() # Marks the starting time

    while Game and Run:
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
            endtime = time.time() - starttime # Marks the ending time
            endtime = round(endtime, 2)
            Game = False  
            Complete = True
        
        pygame.display.update()
        
        if Ball1.ypos >= 570 or Ball2.ypos >= 570:
            Game = False
            time.sleep(3)
        
        clock.tick(60)
        


    if Complete:
        # Splits the leaderboard into lines
        file = open('Leaderboard.txt', 'r')
        leaderboard = file.read().split('\n')
        file.close()   
        
        # Each of these splits a line into name and time
        leaderboard1 = leaderboard[0]
        leaderboard1 = leaderboard1.split(':')

        leaderboard2 = leaderboard[1]
        leaderboard2 = leaderboard2.split(':')

        leaderboard3 = leaderboard[2]
        leaderboard3 = leaderboard3.split(':')

        leaderboard4 = leaderboard[3]
        leaderboard4 = leaderboard4.split(':')

        leaderboard5 = leaderboard[4]
        leaderboard5 = leaderboard5.split(':')

        leaderboard6 = leaderboard[5]
        leaderboard6 = leaderboard6.split(':')

        leaderboard7 = leaderboard[6]
        leaderboard7 = leaderboard7.split(':')

        leaderboard8 = leaderboard[7]
        leaderboard8 = leaderboard8.split(':')

        leaderboard9 = leaderboard[8]
        leaderboard9 = leaderboard9.split(':')

        leaderboard10 = leaderboard[9]
        leaderboard10 = leaderboard10.split(':')
            
        # Each of these adds a time in correct spot
        if endtime < int(leaderboard1[1]):
            movedown(0)
            delete_extra_line()
            replaceline(0)
            
        elif endtime < int(leaderboard2[1]):
            movedown(1)
            delete_extra_line()
            replaceline(1)
            
        elif endtime < int(leaderboard3[1]):
            movedown(2)
            delete_extra_line()
            replaceline(2)
            
        elif endtime < int(leaderboard4[1]):
            movedown(3)
            delete_extra_line()
            replaceline(3)
            
        elif endtime < int(leaderboard5[1]):
            movedown(4)
            delete_extra_line()
            replaceline(4)
            
        elif endtime < int(leaderboard6[1]):
            movedown(5)
            delete_extra_line()
            replaceline(5)
            
        elif endtime < int(leaderboard7[1]):
            movedown(6)
            delete_extra_line()
            replaceline(6)
            
        elif endtime < int(leaderboard8[1]):
            movedown(7)
            delete_extra_line()
            replaceline(7)
            
        elif endtime < int(leaderboard9[1]):
            movedown(8)
            delete_extra_line()
            replaceline(8)
            
        elif endtime < int(leaderboard10[1]):
            movedown(9)
            delete_extra_line()
            replaceline(9)
        
    while Leaderboard and Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
        
        file = open('Leaderboard.txt', 'r')
        leaderboard_str = file.read()
        file.close()
        
        screen.fill(WHITE)
        
        leaderboard_lines = leaderboard_str.splitlines()
        y_offset = 100
        
        for line in leaderboard_lines:
            leaderboard_text = leaderboardfont.render(line, True, BLUE)
            screen.blit(leaderboard_text, (370, y_offset))
            y_offset += 40
        
        return1 = Button(750, 500, 200, 50, "Return", 805, 512)

        return1.DrawButton()
        
        pygame.display.update()

        if pygame.mouse.get_pressed()[0] == 1:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if 750 <= mouse_x <= 950 and 500 <= mouse_y <= 550:
                Screen = True
                Leaderboard = False
    
pygame.quit()