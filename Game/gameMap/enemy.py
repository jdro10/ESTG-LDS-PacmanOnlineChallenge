import pygame

from settings import *

vec = pygame.math.Vector2

class Enemy:
    def __init__(self,app,pos,number):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = 8
        self.number = number
        self.color = self.set_color()

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen,self.color,(int(self.pix_pos.x),int(self.pix_pos.y)),self.radius)

    def get_pix_pos(self):
        return  vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_SPACE//2+self.app.cell_width//2,
                             (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_SPACE//2+self.app.cell_height//2)

    def set_color(self):
        if self.number == 0:
            return BLUE
        elif self.number == 1:
            return RED
        elif self.number == 2:
            return GREEN
        elif self.number == 3:
            return WHITE