import pygame
from random import randint

pygame.init()

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pacman')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
pacmanVermelho_x = 400
pacmanVermelho_y = 400
pacmanVermelho_x_change = 0
pacmanVermelho_y_change = 0

clock = pygame.time.Clock()

x = 0
y = 0

vertical = True

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            if event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            if event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    if(vertical):
        pacmanVermelho_y_change += randint(-1 , 1)
        pacmanVermelho_x_change += 0
        vertical = False
    else:
        pacmanVermelho_y_change += 0
        pacmanVermelho_x_change += randint(-1 , 1)
        vertical = True


    pacmanVermelho_x += pacmanVermelho_x_change
    pacmanVermelho_y += pacmanVermelho_y_change

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(black)
    ##pacman(x, y)
    pygame.draw.rect(gameDisplay, yellow, [lead_x, lead_y, 10, 10]) ##[coordenada a desenhar,coordenada a desenhar, altura, largura]
    pygame.draw.rect(gameDisplay, red, [pacmanVermelho_x, pacmanVermelho_y, 10, 10])
    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()