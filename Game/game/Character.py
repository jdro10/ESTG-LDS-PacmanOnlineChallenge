import pygame

class Character:
    def __init__(self,position_x, position_y,image):
        self.position_x = position_x
        self.position_y = position_y
        self.image = pygame.transform.scale(image,(20,20))

    def get_img(self):
        return self.image

    def set_x(self,coord):
        self.position_x = coord

    def get_x(self):
        return self.position_x

    def set_y(self,coord):
        self.position_y = coord

    def get_y(self):
        return self.position_y