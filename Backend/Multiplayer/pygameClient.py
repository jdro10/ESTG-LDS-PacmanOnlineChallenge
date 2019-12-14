import pygame
import socket
import time

HOST = '192.168.1.65'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

pygame.init()

gamedisplay = pygame.display.set_mode((640, 480))

red = (255, 0, 0)

pygame.display.set_caption('Multiplayer')

clock = pygame.time.Clock()

gameExit = True
x = 250
y = 250
lead_x_change = 0
lead_y_change = 0

while gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    x += lead_x_change
    y += lead_y_change
    
    varx = str(x) + "/" + str(y)
    var = bytes(varx, "utf-8")
    s.sendall(var)
	
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    print("\n")

    gamedisplay.fill((0,0,0))
    pygame.draw.rect(gamedisplay, red, [x, y, 10, 10])

    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()