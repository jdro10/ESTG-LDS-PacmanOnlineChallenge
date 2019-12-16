import pygame
from random import randint

import Colors


class GameLoop:

    def loop(self, gameDisplay, pacman,redGhost):

        lead_x = 300
        lead_y = 300
        lead_x_change = 0
        lead_y_change = 0
        pacmanVermelho_x = 400
        pacmanVermelho_y = 400

        clock = pygame.time.Clock()

        vertical = True

        gameExit = False

        direction = "right"

        pacmanImage = pacman.get_img()

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        lead_x_change = -10
                        lead_y_change = 0
                    if event.key == pygame.K_RIGHT:
                        direction = "right"
                        lead_x_change = 10
                        lead_y_change = 0
                    if event.key == pygame.K_UP:
                        direction = "up"
                        lead_y_change = -10
                        lead_x_change = 0
                    if event.key == pygame.K_DOWN:
                        direction = "down"
                        lead_y_change = 10
                        lead_x_change = 0


            if (vertical):
                pacmanVermelho_y_change = randint(-10, 10)
                pacmanVermelho_x_change = 0
                vertical = False
            else:
                pacmanVermelho_y_change = 0
                pacmanVermelho_x_change = randint(-10, 10)
                vertical = True

            if pacmanVermelho_x + pacmanVermelho_x_change > 780 or pacmanVermelho_x + pacmanVermelho_x_change < 0:
                pacmanVermelho_x_change = 0

            if pacmanVermelho_y + pacmanVermelho_y_change > 580 or pacmanVermelho_y + pacmanVermelho_y_change < 0:
                pacmanVermelho_y_change = 0

            if lead_x + lead_x_change > 780 or lead_x + lead_x_change < 0:
                lead_x_change = 0

            if lead_y + lead_y_change > 580 or lead_y + lead_y_change < 0:
                lead_y_change = 0

            pacmanVermelho_x += pacmanVermelho_x_change
            pacmanVermelho_y += pacmanVermelho_y_change

            lead_x += lead_x_change
            lead_y += lead_y_change

            pacman.set_x(lead_x)
            pacman.set_y(lead_y)

            redGhost.set_x(pacmanVermelho_x)
            redGhost.set_y(pacmanVermelho_y)

            gameDisplay.fill(Colors.black)

            if direction == "right":
                pacmanHead = pacmanImage
            if direction == "left":
                pacmanHead = pygame.transform.flip(pacmanImage, True,False)
            if direction == "up":
                pacmanHead = pygame.transform.rotate(pacmanImage, 90)
            if direction == "down":
                pacmanHead = pygame.transform.rotate(pacmanImage, 270)

            gameDisplay.blit(redGhost.get_img(),(redGhost.get_x(),redGhost.get_y()))
            gameDisplay.blit(pacmanHead, (pacman.get_x(), pacman.get_y()))
            pygame.display.update()

            clock.tick(20)
