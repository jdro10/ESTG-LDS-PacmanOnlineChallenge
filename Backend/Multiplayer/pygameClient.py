import pygame
import socket
import time

HOST = '172.20.131.117'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

pygame.init()

gamedisplay = pygame.display.set_mode((640, 480))

red = (255, 0, 0)
white = (255, 255, 255)

pygame.display.set_caption('Multiplayer')

clock = pygame.time.Clock()

gameExit = True
x = 255
y = 255
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
    msg2= msg.decode('utf-8').split("/");
    msg3 = int(msg2[0])
    msg4 = int(msg2[1])
    print("(", msg3, "/", msg4, ")")

    gamedisplay.fill((0,0,0))
    pygame.draw.rect(gamedisplay, red, [x, y, 10, 10])
    pygame.draw.rect(gamedisplay, white, [int(msg3), int(msg4), 10, 10])

    lead_x_change = 0
    lead_y_change = 0

    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()
