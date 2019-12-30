import pygame
from MenuInstrucoes import menuInstrucoes
from MenuMultiplayer import menuMultiplayer
from game import *

clock = pygame.time.Clock()
clock.tick(5)
pygame.init()

run = Game()

pygame.display.set_caption('PACMAN ONLINE CHALLENGE')
WIDTH, HEIGHT = 610, 670
TOP_BOTTOM_SPACE = 50
MAP_WIDTH, MAP_HEIGHT = WIDTH - TOP_BOTTOM_SPACE, HEIGHT - TOP_BOTTOM_SPACE

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

TEXT_SIZE_MENU = 30
FONT_MENU = 'PAC-FONT.TTF'
TITLE_SIZE = 26
TEXT_SIZE_GAME = 13
FONT_GAME = 'arial black'
posFirstOption = (WIDTH // 2 - 50, HEIGHT // 2 + 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load('img/pacman.png')


def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.Font(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)


def menuPrincipal():
    Running = True
    pos_y_pacman = HEIGHT // 2 + 30
    while Running:
        screen.fill(BLACK)
        draw_text('PACMAM ONLINE', screen, [
            WIDTH // 2, HEIGHT // 2 - 140], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('CHALLENGE', screen, [
            WIDTH // 2, HEIGHT // 2 - 100], TITLE_SIZE, FONT_MENU, YELLOW)
        draw_text('SINGLE PLAYER', screen, [
            WIDTH // 2, HEIGHT // 2 + 50], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        draw_text('MULTIPLAYER', screen, [
            WIDTH // 2, HEIGHT // 2 + 100], TEXT_SIZE_MENU, FONT_MENU, RED)
        draw_text('INSTRUCTIONS', screen, [
            WIDTH // 2, HEIGHT // 2 + 150], TEXT_SIZE_MENU, FONT_MENU, GREEN)
        draw_text('STATS', screen, [
            WIDTH // 2, HEIGHT // 2 + 200], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        screen.blit(pygame.transform.scale(img, (70, 70)),
                    (WIDTH // 3 - 130, pos_y_pacman))

        try:
            j = pygame.joystick.Joystick(0)
            j.init()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                if event.type == pygame.JOYAXISMOTION:
                    if j.get_hat(0) == (0, -1):
                        if ((pos_y_pacman + 50 <= HEIGHT // 2 + 180)):
                            pos_y_pacman += 50
                    elif j.get_hat(0) == (0, 1):
                        if ((pos_y_pacman - 50 >= HEIGHT // 2 + 30)):
                            pos_y_pacman += -50
                    elif j.get_button(1) == 1:
                        select_menu(pos_y_pacman)

        except:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if ((pos_y_pacman + 50 <= HEIGHT // 2 + 180)):
                            pos_y_pacman += 50
                    elif event.key == pygame.K_UP:
                        if ((pos_y_pacman - 50 >= HEIGHT // 2 + 30)):
                            pos_y_pacman += -50
                    elif event.key == pygame.K_RETURN:
                        select_menu(pos_y_pacman)

        pygame.display.update()


def select_menu(pos_y_pacman):
    if pos_y_pacman == (HEIGHT // 2 + 30):
        run.run()
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 50):
        menuMultiplayer()
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 100):
        menuInstrucoes()
    if pos_y_pacman == ((HEIGHT // 2 + 30) + 150):
        print("4")


menuPrincipal()
