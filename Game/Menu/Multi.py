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
green = (0, 255, 0)
blue = (0, 0, 128)

TEXT_SIZE_MENU = 30
FONT_MENU = 'PacFont'
TITLE_SIZE = 26
TEXT_SIZE_GAME = 13
FONT_GAME = 'arial black'

#window configuration
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Choose character')

#game config
clock = pygame.time.Clock()
Running = True

#images
pacman = pygame.image.load('pacman.png')
ghost = pygame.image.load('vermelho.png')
ghost = pygame.transform.scale(ghost, (180, 180))






xis = (display_width * 0.65)
ypslon = (display_height * 0.38)

x =  (display_width * 0.1)
y = (display_height * 0.35)


def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.SysFont(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    gameDisplay.fill(black)
    gameDisplay.blit(pacman, (x, y))
    gameDisplay.blit(ghost, (xis, ypslon))
    draw_text('CHOOSE YOUR CHARACTER !', gameDisplay, [display_width // 2, display_height // 2 - 140], TITLE_SIZE, FONT_MENU, white)


    pygame.display.update()
    clock.tick(60)
