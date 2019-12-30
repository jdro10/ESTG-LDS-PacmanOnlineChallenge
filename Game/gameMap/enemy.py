
import pygame, random

from settings import *

vec = pygame.math.Vector2

class Enemy:
    def __init__(self,app,pos,number):
        self.app = app
        self.grid_pos = pos
        self.starting_pos = [pos.x, pos.y]
        self.pix_pos = self.get_pix_pos()
        self.radius = 8
        self.number = number
        self.color = self.set_color()
        self.direction = vec(0,0)  #POR A MOVER LOGO
        self.type = self.set_type()
        self.target = None
        self.speed = self.set_speed()
        self.image = self.set_image()


    def update(self):
        self.target = self.set_target()
        if self.target != self.grid_pos:
            self.pix_pos += self.direction*self.speed
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

    def set_speed(self):
        if self.type in ["fast chaser","fast random"]:
            speed = 2
        else:
            speed = 1

        return speed

    def set_target(self):
        if self.type == "slow chaser" or self.type == "fast chaser":
            return self.app.pacman.grid_pos
        else:
            if self.app.pacman.grid_pos[0] > NUMBER_CELLS_WIDTH // 2 and self.app.pacman.grid_pos[1] > NUMBER_CELLS_HEIGHT // 2:
                return vec(1,1)
            if self.app.pacman.grid_pos[0] > NUMBER_CELLS_WIDTH // 2 and self.app.pacman.grid_pos[1] < NUMBER_CELLS_HEIGHT // 2:
                return vec(1,NUMBER_CELLS_HEIGHT-2)
            if self.app.pacman.grid_pos[0] < NUMBER_CELLS_WIDTH // 2 and self.app.pacman.grid_pos[1] > NUMBER_CELLS_HEIGHT // 2:
                return vec(NUMBER_CELLS_WIDTH-2,1)
            else:
                return vec(NUMBER_CELLS_WIDTH-2,NUMBER_CELLS_HEIGHT-2)

    def draw(self):
        #pygame.draw.circle(self.app.screen,self.color,(int(self.pix_pos.x),int(self.pix_pos.y)),self.radius) #BEM

        if (self.number == 0):
            self.app.screen.blit(self.app.redGhost, (int(self.pix_pos.x - 8), int(self.pix_pos.y - 8)))
        elif (self.number == 1):
            self.app.screen.blit(self.app.blueGhost, (int(self.pix_pos.x - 8), int(self.pix_pos.y - 8)))
        elif (self.number == 2):
            self.app.screen.blit(self.app.greenGhost, (int(self.pix_pos.x - 8), int(self.pix_pos.y - 8)))
        elif (self.number == 3):
            self.app.screen.blit(self.app.pinkGhost, (int(self.pix_pos.x - 8), int(self.pix_pos.y - 8)))

        #pygame.draw.(self.app.screen,self.image,(int(self.pix_pos.x)),int(self.pix_pos.y))
        #self.app.screen.blit(self.get_img(),(10,10))

    def get_pix_pos(self):
        return  vec(((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_SPACE//2+self.app.cell_width//2),
                    ((self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_SPACE//2+self.app.cell_height//2))


    def get_img(self):
        return self.image

    def set_type(self):
        if self.number == 0:
            return "fast chaser"
        elif self.number == 1:
            return "slow chaser"
        elif self.number == 2:
            return "fast random"
        else:
            return "slow random"

    #def get_type(self):
        #return self.type

    def set_color(self):
        if self.number == 0:
            return BLUE
        elif self.number == 1:
            return RED
        elif self.number == 2:
            return GREEN
        elif self.number == 3:
            return WHITE

    def set_image(self):
        if self.number == 0:
            image = pygame.image.load("img/verde.png")
            image = pygame.transform.scale(image,(8,6))
            self.image = image
        elif self.number == 1:
            image = pygame.image.load("img/vermelho.png")
            image = pygame.transform.scale(image, (8, 6))
            self.image = image
        elif self.number == 2:
            image = pygame.image.load("img/rosa.png")
            image = pygame.transform.scale(image, (8, 6))
            self.image = image
        elif self.number == 3:
            image = pygame.image.load("img/azul.png")
            image = pygame.transform.scale(image, (8, 6))
            self.image = image


    def time_to_move_x(self):
        if int(self.pix_pos.x+TOP_BOTTOM_SPACE//2)%self.app.cell_width==0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0) or self.direction == vec(0,0):
                return True

    def time_to_move_y(self):
        if int(self.pix_pos.y+TOP_BOTTOM_SPACE//2)%self.app.cell_height==0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1) or self.direction == vec(0,0):
                return True

    def move(self):
        if self.type == "slow random":
            self.direction = self.get_random_direction()
        elif self.type == "slow chaser":
            self.direction = self.get_pacman_direction(self.target)
        elif self.type == "fast random":
            self.direction = self.get_pacman_direction(self.target)
        else :
            self.direction = self.get_pacman_direction(self.target)


    def get_pacman_direction(self,target):
        next_cell = self.find_next_cell(target)
        x_dir = next_cell[0] - self.grid_pos[0]
        y_dir = next_cell[1] - self.grid_pos[1]
        return vec(x_dir,y_dir)

    def find_next_cell(self,target):
        path = self.get_pacman_path([int(self.grid_pos.x), int(self.grid_pos.y)],[int(target[0]),int(target[1])])
        return path[1]


    #buscarposiçaopacman
    def get_pacman_path(self,start,target):
        grid = [[0 for x in range(NUMBER_CELLS_WIDTH)] for x in range(NUMBER_CELLS_HEIGHT)]
        for cell in self.app.walls:
            if cell.x < NUMBER_CELLS_WIDTH and cell.y < NUMBER_CELLS_HEIGHT:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest

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
            next_pos = vec(self.grid_pos.x +  x_dir , self .grid_pos.y + y_dir)
            if next_pos not in self.app.walls:
                break

        return vec(x_dir,y_dir)