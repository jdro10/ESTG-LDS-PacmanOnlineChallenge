import pygame

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
img = pygame.image.load('inst.png')

def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.SysFont(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)


#### MENU ####
def start_draw1():
    Running = True
    while Running:
        screen.fill(WHITE)
        draw_text('PACMAM ONLINE', screen, [WIDTH // 2, HEIGHT // 2-250], TITLE_SIZE, FONT_MENU, BLUE)
        draw_text('CHALLENGE', screen, [WIDTH // 2, HEIGHT // 2 - 210], TITLE_SIZE, FONT_MENU, BLUE)

        screen.blit(pygame.transform.scale(img, (625,348)), (WIDTH // 2-300, HEIGHT // 2 -90))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Running = False
                if event.key == pygame.K_RETURN:
                    Running = False


            pygame.display.update()