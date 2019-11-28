import pygame
from pacmanPygame.Display import Display
from pacmanPygame.GameLoop import GameLoop
from pacmanPygame.Character import Character

imgPacman = pygame.image.load("pacman.png")

pacman = Character(300,300,imgPacman)

imgRedGhost = pygame.image.load("redghost.png")

redGhost = Character(200,100,imgRedGhost)

display = Display()

window = display.display()

singlePlayer = GameLoop()

singlePlayer.loop(window,pacman,redGhost)