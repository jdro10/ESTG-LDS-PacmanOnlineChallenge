import pygame , sys
from pacman import *
from  enemy import *

pygame.init()

vec = pygame.math.Vector2

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock  = pygame.time.Clock()
        self.gameLoop = True
        self.state = 'menu'
        self.cell_width = MAP_WIDTH//NUMBER_CELLS_WIDTH
        self.cell_height = MAP_HEIGHT//NUMBER_CELLS_HEIGHT
        self.pacman_position = None
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.pacman_position = None
        self.load()
        self.pacman = Pacman(self, vec(self.pacman_position))
        self.make_enemies()
        self.gameOverLoop = True






    #### GAME LOOP ####
    def run(self):
        while self.gameLoop:
            if self.state == 'menu':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playsingle':
                self.playsingle_events()
                self.playsingle_update()
                self.playsingle_draw()
            elif self.state == 'game over':
                self.gameover_events()
                self.gameover_update()
                self.gameover_draw()
            else:
                self.gameLoop = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


    def draw_text(self, message, screen, position, size, font_type, color):
        font = pygame.font.SysFont(font_type , size)
        text = font.render(message, False, color)
        text_size = text.get_size()
        position[0] = position[0]-text_size[0]//2
        screen.blit(text, position)

    #### EVENTS KEYS ####
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameLoop = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playsingle'

    def start_update(self):
        pass

    #### MENU ####
    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PACMAM ONLINE', self.screen, [WIDTH // 2, HEIGHT // 2-140], TITLE_SIZE, FONT_MENU, YELLOW)
        self.draw_text('CHALLENGE', self.screen, [WIDTH // 2, HEIGHT // 2 - 100], TITLE_SIZE, FONT_MENU, YELLOW)
        self.draw_text('SINGLE PLAYER', self.screen, [WIDTH // 2, HEIGHT // 2+50], TEXT_SIZE_MENU, FONT_MENU, BLUE)
        self.draw_text('MULTIPLAYER', self.screen, [WIDTH // 2, HEIGHT // 2 + 100], TEXT_SIZE_MENU, FONT_MENU, RED)
        self.draw_text('INSTRUCTIONS', self.screen, [WIDTH // 2, HEIGHT // 2 + 150], TEXT_SIZE_MENU, FONT_MENU, GREEN)
        pygame.display.update()

    def playsingle_events(self):

        try:
            j = pygame.joystick.Joystick(0)
            j.init()

            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if j.get_axis(0) > 0.2:
                        self.pacman.move(vec(1,0))
                    elif j.get_axis(0) < -0.2:
                        self.pacman.move(vec(-1,0))
                    elif j.get_axis(1) > 0.2:
                        self.pacman.move(vec(0,1))
                    elif j.get_axis(1) < -0.2:
                        self.pacman.move(vec(0,-1))
                    elif j.get_hat(0) == (0 , 1):
                        self.pacman.move(vec(0,-1))
                    elif j.get_hat(0) == (0 , -1):
                        self.pacman.move(vec(0,1))
                    elif j.get_hat(0) == (1 , 0):
                        self.pacman.move(vec(1,0))
                    elif j.get_hat(0) == (-1 , 0):
                        self.pacman.move(vec(-1,0))

        except:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pacman.move(vec(-1,0))
                    elif event.key == pygame.K_RIGHT:
                        self.pacman.move(vec(1, 0))
                    elif event.key == pygame.K_DOWN:
                        self.pacman.move(vec(0, 1))
                    elif event.key == pygame.K_UP:
                        self.pacman.move(vec(0, -1))


    def playsingle_update(self):
        self.pacman.update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if enemy.grid_pos == self.pacman.grid_pos:
                self.remove_life()

    def playsingle_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background,(TOP_BOTTOM_SPACE//2,TOP_BOTTOM_SPACE//2))
        self.draw_coins()
        #self.draw_grid() #REDE
        self.draw_text('CURRENT SCORE : {}'.format(self.pacman.score), self.screen, [100,0], TEXT_SIZE_GAME, FONT_GAME, WHITE)
        self.draw_text('TIME : 0', self.screen, [550, 0], TEXT_SIZE_GAME, FONT_GAME, WHITE)
        self.draw_text('PACMAN ONLINE CHALLENGE', self.screen, [WIDTH//2, 650], TEXT_SIZE_GAME, FONT_GAME, YELLOW)
        self.pacman.draw()
        #self.screen.blit(self.yellowPacman,self.pacman.get_pix_pos())
        for enemy in self.enemies:
            #enemy.draw()

            if(enemy.number == 0):
                self.screen.blit(self.redGhost,((enemy.get_pix_pos()[0]-8),enemy.get_pix_pos()[1]-8))
            elif(enemy.number == 1):
                self.screen.blit(self.greenGhost,((enemy.get_pix_pos()[0]-8),enemy.get_pix_pos()[1]-8))
            elif(enemy.number == 2):
                self.screen.blit(self.pinkGhost,((enemy.get_pix_pos()[0]-8),enemy.get_pix_pos()[1]-8))
            elif(enemy.number == 3):
                self.screen.blit(self.blueGhost,((enemy.get_pix_pos()[0]-8),enemy.get_pix_pos()[1]-8))

        pygame.display.update()
        #self.coins.pop()

    def remove_life(self):
        self.pacman.lives -= 1
        if self.pacman.lives == 0:
            self.state = "game over"
        else:
            self.pacman.grid_pos = vec(self.pacman.starting_position)
            self.pacman.pixel_pos = self.pacman.get_pix_pos()
            self.pacman.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            #pygame.draw.circle(self.screen,LIGHT_YELLOW, (int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_SPACE//2,int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_SPACE//2),4)
            self.screen.blit(self.coin, ((int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_SPACE//2)-8,
                                         (int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_SPACE//2)-8))

    def draw_grid(self):
        for x in range (WIDTH//self.cell_width):
            pygame.draw.line(self.background, WHITE , (x*self.cell_width,0), (x*self.cell_width, HEIGHT))
        for x in range (HEIGHT//self.cell_height):
            pygame.draw.line(self.background, WHITE , (0 , x*self.cell_height), (WIDTH, x*self.cell_height))
        for coin in self.coins:
            pygame.draw.rect(self.background, GREEN, (coin.x*self.cell_width,coin.y*self.cell_height,self.cell_width,self.cell_height))


    #def coin_sound(self):
        #pygame.mixer.Sound.play(self.coin_sound)


    def load(self):
        self.background = pygame.image.load('maze.png')
        self.redGhost = pygame.image.load('vermelho.png')
        self.redGhost = pygame.transform.scale(self.redGhost,(14,14))
        self.blueGhost = pygame.image.load('azul.png')
        self.blueGhost = pygame.transform.scale(self.blueGhost,(14, 14))
        self.greenGhost = pygame.image.load('verde.png')
        self.greenGhost = pygame.transform.scale(self.greenGhost,(14, 14))
        self.pinkGhost = pygame.image.load('rosa.png')
        self.pinkGhost = pygame.transform.scale(self.pinkGhost,(14, 14))
        self.yellowPacman = pygame.image.load('pacman.png')
        self.yellowPacman = pygame.transform.scale(self.yellowPacman,(20,20))
        self.coin = pygame.image.load('star.png')
        self.coin = pygame.transform.scale(self.coin,(10,10))
        self.coin_sound = pygame.mixer.Sound('coin.wav')
        self.gameover_sound = pygame.mixer.Sound('gameover.wav')

        #HA FALTA DE MELHOR VAI TER QUE SER ASSIM com a string
        self.background = pygame.transform.scale(self.background, (MAP_WIDTH, MAP_HEIGHT))
        #settings wall while opening and characters / coins
        with open("walls.txt",'r') as fp:
            for yindex,line in enumerate(fp):
                for xindex,char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xindex,yindex))
                    elif char == "C":
                        self.coins.append(vec(xindex,yindex))
                    elif char == "P":
                        self.pacman_position = [xindex,yindex]
                    elif char  in ["2","3","4","5"]:
                        self.e_pos.append([xindex,yindex])
                    elif char == "B":
                        pygame.draw.rect(self.background,BLACK , (xindex*self.cell_width,yindex*self.cell_height,self.cell_width,self.cell_height))



    def make_enemies(self):
        for xindex ,pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self,vec(pos),xindex))

############################# GAME OVER ############################################

    def gameover_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def gameover_update(self):
        pass

    def gameover_draw(self):
        if self.gameOverLoop:
            pygame.mixer.Sound.play(self.gameover_sound)
            self.gameOverLoop = False
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER",self.screen,[WIDTH//2,100],36,FONT_MENU,RED)
        pygame.display.update()


    def reset(self):
        self.pacman.lives = 3
        self.coins = [] ## por a zero
        self.pacman.score = 0
        self.pacman.grid_pos = vec (self.pacman.starting_position)
        self.pacman.pix_pos = self.pacman.get_pix_pos()
        self.pacman.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0
        with open("walls.txt",'r') as fp:
            for yindex,line in enumerate(fp):
                for xindex,char in enumerate(line):
                    if char == "C":
                        self.coins.append(vec(xindex,yindex))
        self.gameOverLoop = True
        self.state = "playsingle"