import pygame

class Display:

    def display(self):

        pygame.init()

        icon = pygame.image.load("pacman.png")

        pygame.display.set_icon(icon)

        gamedisplay = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Pacman')

        return gamedisplay