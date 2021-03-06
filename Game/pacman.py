import pygame
vec = pygame.math.Vector2
from settings import *

class Pacman:
    def __init__(self, app, pos):
        self.app = app
        self.starting_position = [pos[0],pos[1]]
        self.grid_pos = vec(pos[0],pos[1])
        self.pixel_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.buffer_direction = None
        self.can_move = True
        self.score = 0
        self.speed = 2
        self.lives = 3


    def update(self):
        if self.can_move:
            self.pixel_pos += self.direction*self.speed

        if self.time_to_move_x():
            if self.buffer_direction != None:
                self.direction = self.buffer_direction
            self.can_move = self.let_move()
        if self.time_to_move_y():
            if self.buffer_direction != None:
                self.direction = self.buffer_direction
            self.can_move = self.let_move()

        self.grid_pos[0] = (self.pixel_pos[0]-TOP_BOTTOM_SPACE+self.app.cell_width//2)//self.app.cell_width + 1
        self.grid_pos[1] = (self.pixel_pos[1] - TOP_BOTTOM_SPACE+self.app.cell_height//2) // self.app.cell_height + 1

        if self.on_Coin():
            self.smash_coin()

    #verifica se estou em cima da moeda
    def on_Coin(self):
        if self.grid_pos in self.app.coins:
            if self.time_to_move_x():
                return True
            if self.time_to_move_y():
                return True

        return False

    def smash_coin(self):
        #pygame.mixer.Sound.stop(self.app.coin_sound)
        self.app.coins.remove(self.grid_pos)
        pygame.mixer.Sound.play(self.app.coin_sound)
        self.score += 10

    def draw(self):
        #pygame.draw.circle(self.app.screen, YELLOW, (int(self.pixel_pos.x), int(self.pixel_pos.y)),self.app.cell_width//2-2)

        if(self.direction == vec(1,0)):
            self.app.screen.blit(self.app.yellowPacman, (int(self.pixel_pos.x - 8), int(self.pixel_pos.y - 8)))
        elif (self.direction == vec(-1, 0)):
            self.app.screen.blit(pygame.transform.flip(self.app.yellowPacman,True, False), (int(self.pixel_pos.x - 8), int(self.pixel_pos.y - 8)))
        elif (self.direction == vec(0, 1)):
            self.app.screen.blit(pygame.transform.rotate(self.app.yellowPacman, 270), (int(self.pixel_pos.x - 8), int(self.pixel_pos.y - 8)))
        elif (self.direction == vec( 0 ,-1)):
            self.app.screen.blit(pygame.transform.rotate(self.app.yellowPacman, 90), (int(self.pixel_pos.x - 8), int(self.pixel_pos.y - 8)))


        for x in range(self.lives):
            self.app.screen.blit(self.app.yellowPacman,(35 + 20*x, HEIGHT - 25))
            #pygame.draw.circle(self.app.screen, YELLOW , (35 + 20*x, HEIGHT - 15),6)
        #DESENHA gajo atras
        #pygame.draw.rect(self.app.screen,RED,
                        # (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_SPACE//2,
                        #  self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_SPACE//2,
                         # self.app.cell_width,self.app.cell_height),
                         # 1)

    def move(self,direction):
        self.buffer_direction = direction

    def get_pix_pos(self):
        return  vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_SPACE//2+self.app.cell_width//2,
                             (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_SPACE//2+self.app.cell_height//2)

    def time_to_move_x(self):
        if int(self.pixel_pos.x+TOP_BOTTOM_SPACE//2)%self.app.cell_width==0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0) or self.direction == vec(0,0):
                return True

    def time_to_move_y(self):
        if int(self.pixel_pos.y+TOP_BOTTOM_SPACE//2)%self.app.cell_height==0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1) or self.direction == vec(0,0):
                return True

    def let_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True