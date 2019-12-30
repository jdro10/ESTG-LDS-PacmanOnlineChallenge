import pygame
from MenuInstrucoes import menuInstrucoes

pygame.init()


def draw_text(message, screen, position, size, font_type, color):
    font = pygame.font.SysFont(font_type, size)
    text = font.render(message, False, color)
    text_size = text.get_size()
    position[0] = position[0] - text_size[0] // 2
    screen.blit(text, position)


def menuMultiplayer():
    display_width = 610
    display_height = 670

    pygame.display.set_caption('PACMAN ONLINE CHALLENGE')

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    TEXT_SIZE_MENU = 30
    FONT_MENU = 'PacFont'
    TITLE_SIZE = 26
    TEXT_SIZE_GAME = 13
    FONT_GAME = 'arial black'

    gameDisplay = pygame.display.set_mode((display_width, display_height))

    clock = pygame.time.Clock()
    Running = True

    pacman = pygame.image.load('img/pacman.png')
    ghost = pygame.image.load('img/vermelho.png')
    seta = pygame.image.load('img/seta.png')
    ghost = pygame.transform.scale(ghost, (180, 180))
    seta = pygame.transform.scale(seta, (180, 150))

    Running = True
    xis = (display_width * 0.65)
    ypslon = (display_height * 0.38)

    x = (display_width * 0.1)
    y = (display_height * 0.35)

    x_seta = (display_width * 0.13)
    y_seta = (display_height * 0.67)
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if x_seta == (display_width * 0.13):
                        x_seta = (display_width * 0.65)
                if event.key == pygame.K_LEFT:
                    if x_seta == (display_width * 0.65):
                        x_seta = (display_width * 0.13)
                if event.key == pygame.K_ESCAPE:
                    Running = False

        gameDisplay.fill(black)
        gameDisplay.blit(pacman, (x, y))
        gameDisplay.blit(ghost, (xis, ypslon))
        gameDisplay.blit(seta, (x_seta, y_seta))
        draw_text('CHOOSE YOUR CHARACTER !', gameDisplay, [
                  display_width // 2, display_height // 2 - 140], TITLE_SIZE, FONT_MENU, white)

        pygame.display.update()
        clock.tick(60)
