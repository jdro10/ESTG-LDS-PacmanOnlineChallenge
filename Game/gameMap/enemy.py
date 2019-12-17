import pygame, random

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
        self.direction = vec(1,0)  #POR A MOVER LOGO
        self.type = self.set_type()

    def update(self):
        self.pix_pos += self.direction
        if self.can_move():
            self.move()

        #gravar as posições
        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_SPACE + self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_SPACE + self.app.cell_height // 2) // self.app.cell_height + 1

    def can_move(self):

        if self.time_to_move_x():
            return True

        if self.time_to_move_y():
            return True

        return False


    def draw(self):
        pygame.draw.circle(self.app.screen,self.color,(int(self.pix_pos.x),int(self.pix_pos.y)),self.radius)

    def get_pix_pos(self):
        return  vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_SPACE//2+self.app.cell_width//2,
                             (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_SPACE//2+self.app.cell_height//2)

    def set_type(self):
        if self.number == 0:
            return "speedy"
        elif self.number == 1:
            return "slow"
        elif self.number == 2:
            return "random"
        else:
            return "top"

    def set_color(self):
        if self.number == 0:
            return BLUE
        elif self.number == 1:
            return RED
        elif self.number == 2:
            return GREEN
        elif self.number == 3:
            return WHITE




    def time_to_move_x(self):
        if int(self.pix_pos.x+TOP_BOTTOM_SPACE//2)%self.app.cell_width==0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                return True

    def time_to_move_y(self):
        if int(self.pix_pos.y+TOP_BOTTOM_SPACE//2)%self.app.cell_height==0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                return True

    def move(self):
        if self.type == "random":
            self.direction = self.get_random_direction()


    def get_random_direction(self):
        while True:
            number = random.randint(-2,1)
            if number == -2:
                x_dir , y_dir = 1,0
            elif number == -1:
                x_dir, y_dir = 0, 1
            elif number == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            break
            direction = vec(x_dir,y_dir)
            #if vec(direction.x+x_dir,direction.y+y_dir) in self.app.walls:
                #break

        return vec(x_dir,y_dir)