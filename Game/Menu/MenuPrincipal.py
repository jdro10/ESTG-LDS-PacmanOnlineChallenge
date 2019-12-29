import pygame
from MenuInstrucoes import start_draw1
from Multi import startDraw

clock = pygame.time.Clock()
clock.tick(5)
pygame.init()


WIDTH, HEIGHT = 600, 1100
TOP_BOTTOM_SPACE = 50
MAP_WIDTH, MAP_HEIGHT = WIDTH - TOP_BOTTOM_SPACE, HEIGHT - TOP_BOTTOM_SPACE

# colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# text type
TEXT_SIZE_MENU = 30
FONT_MENU = 'PacFont'
TITLE_SIZE = 26
TEXT_SIZE_GAME = 13
FONT_GAME = 'arial black'
posFirstOption = (WIDTH // 2 - 50, HEIGHT // 2 + 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('pacman.png')


def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.SysFont(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)


#### MENU ####
def start_draw():
    Running = True
    pos_y_pacman = HEIGHT // 2 + 30
    while Running:
        screen.fill(BLACK)
        draw_text('PACMAM ONLINE', screen, [WIDTH // 2, HEIGHT // 2 - 140], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('CHALLENGE', screen, [WIDTH // 2, HEIGHT // 2 - 100], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('SINGLE PLAYER', screen, [WIDTH // 2, HEIGHT // 2 + 50], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        draw_text('MULTIPLAYER', screen, [WIDTH // 2, HEIGHT // 2 + 100], TEXT_SIZE_MENU, FONT_MENU, RED)
        draw_text('INSTRUCTIONS', screen, [WIDTH // 2, HEIGHT // 2 + 150], TEXT_SIZE_MENU, FONT_MENU, GREEN)
        draw_text('STATS', screen, [WIDTH // 2, HEIGHT // 2 + 200], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        screen.blit(pygame.transform.scale(img, (70, 70)), (WIDTH // 3 - 130, pos_y_pacman))
        pygame.mixer.music.load('song.wav')
        pygame.mixer.music.play(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if ((pos_y_pacman + 50 <= HEIGHT // 2 + 180)):
                        pos_y_pacman += 50
                if event.key == pygame.K_UP:
                    if ((pos_y_pacman - 50 >= HEIGHT // 2 + 30)):
                        pos_y_pacman += -50
                if event.key == pygame.K_RETURN:
                    select_menu(pos_y_pacman)

        pygame.display.update()


def select_menu(pos_y_pacman):
    if pos_y_pacman == (HEIGHT // 2 + 30):
        print("1")
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 50):
        startDraw()
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 100):
        start_draw1()
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 150):
        print("4")


start_draw()

