import pygame
clock = pygame.time.Clock()
clock.tick(5)
pygame.init()

WIDTH , HEIGHT = 610 , 1000
TOP_BOTTOM_SPACE = 10
MAP_WIDTH , MAP_HEIGHT = WIDTH-TOP_BOTTOM_SPACE , HEIGHT-TOP_BOTTOM_SPACE

#colors
BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

#text type
TEXT_SIZE_MENU = 30
FONT_MENU = 'PacFont'
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
        screen.fill(BLACK)
        #draw_text('PACMAM ONLINE', screen, [WIDTH // 2, HEIGHT // 2-250], TITLE_SIZE, FONT_MENU, BLUE)
        #draw_text('CHALLENGE', screen, [WIDTH // 2, HEIGHT // 2 - 210], TITLE_SIZE, FONT_MENU, BLUE)

        screen.blit(pygame.transform.scale(img, (610,1000)), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Running = False
                if event.key == pygame.K_RETURN:
                    Running = False


            pygame.display.update()