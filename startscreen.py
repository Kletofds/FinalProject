import pygame,sys
from pygame import *
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

size = (1000,600)
screen = pygame.display.set_mode(size)

buttonfont = pygame.font.Font(None, 40)
titlefont = pygame.font.Font(None, 100)

Run = True

button_x = 400
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
        button_rect = pygame.Rect(self.rectypos, self.rectxpos, self.rect_width, self.rect_height)
        
        pygame.draw.rect(screen, BLACK, button_rect)
        
        button_text = buttonfont.render(self.text, True, WHITE)
        
        screen.blit(button_text, (426, 313))

while Run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(WHITE)
    
    button = Button(button_x, button_y, 200, 50, "Start Game")

    button.DrawButton()
    
    title_text = titlefont.render("Two-gether Roll", True, BLUE)
    screen.blit(title_text, (245, 100))
    
    pygame.display.update()

    if pygame.mouse.get_pressed()[0] == 1:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
            pygame.quit()
            Run = False
