import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.font = pg.font.SysFont('Arial', 25)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            password = ''
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                    print("123")
                    print(password)
                elif event.key == pg.K_BACKSPACE:
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
        pg.draw.rect(screen, self.color, self.rect, 2)

    def addText(self):
        screen.blit(pg.font.SysFont('PacFont', 25).render(
            'login', True, (255, 0, 0)), (260, 300))


def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(200, 200, 140, 32)
    input_box2 = InputBox(200, 250, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        button = pg.Rect(260, 300, 100, 40)
        pg.draw.rect(screen, [255, 255, 255], button)
        InputBox.addText(screen)
        img = pg.image.load('img/logo.png')
        screen.blit(pg.transform.scale(img, (200, 150)), (200, 10))
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
