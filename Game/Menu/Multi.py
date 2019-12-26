import pygame
from MenuInstrucoes import start_draw1

#clock = pygame.time.Clock()
#clock.tick(5)
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Choose character')