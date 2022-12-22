import pygame,sys
from pygame import *
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (800,600)
screen = pygame.display.set_mode(size)

font = pygame.font.Font(None, 24)

Run = True

button_x = 300
button_y = 300
button_width = 200
button_height = 50

class Button:
    def __init__(self, rectypos, rectxpos, rect_width, rect_height, text):
        self.rectypos = rectypos
        self.rectxpos = rectxpos
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.text = text
        
    def DrawButton(self):
        pygame.draw.rect(screen, WHITE, (self.rectypos, self.rectxpos, self.rect_width, self.rect_height))
        
        text_surface = font.render(self.text, True, BLACK)

        text_width, text_height = font.size(self.text)

        text_x = self.rectxpos + (self.rect_width - text_width) / 2
        text_y = self.rectypos + (self.rect_height - text_height) / 2

        screen.blit(text_surface, (text_x, text_y))

while Run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(BLACK)
    
    button = Button(button_x, button_y, 200, 50, "Start Game")

    button.DrawButton()
    
    pygame.display.update()

    if pygame.mouse.get_pressed()[0] == 1:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if button_y <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
            pygame.quit()
            Run = False
