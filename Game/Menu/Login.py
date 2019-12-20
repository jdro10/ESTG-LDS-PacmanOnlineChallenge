import pygame


def main():
    WHITE = (255,255,255)
    YELLOW = (173,255,47)
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color(WHITE)
    color_active = pygame.Color(YELLOW)
    color = color_inactive
    active = False
    boxPass = ''
    password = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(password)
                        boxPass = ''
                    elif event.key == pygame.K_BACKSPACE:
                        boxPass = boxPass[:-1]
                        password = password[:-1]
                    else:
                        password += event.unicode
                        boxPass += '*'

        screen.fill((30, 30, 30))

        txt_surface = font.render(boxPass, True, color)

        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()