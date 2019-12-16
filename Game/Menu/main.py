import pygame , sys

pygame.init()

WIDTH , HEIGHT = 610 , 670
TOP_BOTTOM_SPACE = 50
MAP_WIDTH , MAP_HEIGHT = WIDTH-TOP_BOTTOM_SPACE , HEIGHT-TOP_BOTTOM_SPACE

#colors
BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

#text type
TEXT_SIZE_MENU = 18
FONT_MENU = 'elephant'
TITLE_SIZE = 26
TEXT_SIZE_GAME = 13
FONT_GAME = 'arial black'
posFirstOption = (WIDTH // 2-50, HEIGHT // 2+30)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
img = pygame.image.load('pacman.png')

def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.SysFont(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)




#### MENU ####
def start_draw():
    pos_y_pacman = HEIGHT // 2 + 30
    while True:
        screen.fill(BLACK)
        draw_text('PACMAM ONLINE', screen, [WIDTH // 2, HEIGHT // 2-140], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('CHALLENGE', screen, [WIDTH // 2, HEIGHT // 2 - 100], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('SINGLE PLAYER', screen, [WIDTH // 2, HEIGHT // 2+50], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        draw_text('MULTIPLAYER', screen, [WIDTH // 2, HEIGHT // 2 + 100], TEXT_SIZE_MENU, FONT_MENU, RED)
        draw_text('INSTRUCTIONS', screen, [WIDTH // 2, HEIGHT // 2 + 150], TEXT_SIZE_MENU, FONT_MENU, GREEN)
        screen.blit(pygame.transform.scale(img, (50, 50)), (WIDTH // 2 - 100, pos_y_pacman))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if((pos_y_pacman + 50 <= HEIGHT // 2 + 130)):
                        pos_y_pacman += 50
                if event.key == pygame.K_UP:
                    if((pos_y_pacman - 50 >= HEIGHT // 2 + 30)):
                        pos_y_pacman += -50

        pygame.display.update()


start_draw()

#first option
##screen.blit(pygame.transform.scale(img, (50, 50)), (WIDTH // 2-100, HEIGHT // 2+30))

#second option
##screen.blit(pygame.transform.scale(img, (50, 50)), (WIDTH // 2-100, HEIGHT // 2+80))

#third option
##screen.blit(pygame.transform.scale(img, (50, 50)), (WIDTH // 2-100, HEIGHT // 2+30))




