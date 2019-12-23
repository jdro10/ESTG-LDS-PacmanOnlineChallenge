import pygame
import socket
import time
import requests

r = requests.get('https://localhost:5001/api/ranks', verify=False)

print(r.text)

HOST = '127.0.0.1'
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
lead_x_change = 0
lead_y_change = 0

playerNumber = 0

personagem = input()

if personagem == 'PACMAN':
    s.sendall(b'255/255')
    x = 255
    y = 255
elif personagem == 'GHOST':
    s.sendall(b'355/355')
    x = 355
    y = 355

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

    myCoord = bytes(str(x)+ "/" + str(y), 'utf-8')
    s.sendall(myCoord)

    otherPlayerCoord = s.recv(1024)
    decode = otherPlayerCoord.decode('utf-8').split("/")
    print(decode)

    x += lead_x_change
    y += lead_y_change

    gamedisplay.fill((0, 0, 0))

    if personagem == 'PACMAN':
        pygame.draw.rect(gamedisplay, red, [x, y, 10, 10])
        pygame.draw.rect(gamedisplay, white, [int(decode[0]), int(decode[1]), 10, 10])
    else:
        pygame.draw.rect(gamedisplay, red, [int(decode[0]), int(decode[1]), 10, 10])
        pygame.draw.rect(gamedisplay, white, [x, y, 10, 10])

    lead_x_change = 0
    lead_y_change = 0

    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()
