import pygame
import requests
import json

data = {'Username':'user101', 'Password':'pass12345'}
headers = {'Content-type': 'application/json'}

response = requests.post('https://localhost:5001/api/user/auth', data = json.dumps(data), headers = headers, verify = False)

print(response.status_code)
print(response.text)

pygame.init()
screen = pygame.display.set_mode((610, 670))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.font = pygame.font.SysFont('Arial', 25)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            password = ''
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                    print("123")
                    print(password)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    password += '*'
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def addText(self):
        screen.blit(pygame.font.SysFont('PacFont', 25).render(
            'login', True, (255, 0, 0)), (260, 300))


def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(200, 200, 140, 32)
    input_box2 = InputBox(200, 250, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        button = pygame.Rect(260, 300, 100, 40)
        pygame.draw.rect(screen, [255, 255, 255], button)
        InputBox.addText(screen)
        img = pygame.image.load('img/logo.png')
        screen.blit(pygame.transform.scale(img, (200, 150)), (200, 10))
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
