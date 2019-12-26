import pygame
from MenuInstrucoes import start_draw1

#clock = pygame.time.Clock()
#clock.tick(5)
pygame.init()

#windows settings
display_width = 800
display_height = 600

#colors
black = (0,0,0)
white = (255,255,255)

#window configuration
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Choose character')

#game config
clock = pygame.time.Clock()
Running = True

#images
pacman = pygame.image.load('pacman.png')
ghost = pygame.image.load('vermelho.png')

def pac(x,y):
    gameDisplay.blit(pacman, (x,y))

x =  (display_width * 0.1)
y = (display_height * 0.35)

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    gameDisplay.fill(black)
    pac(x, y)

    pygame.display.update()
    clock.tick(60)
