import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Pers(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("pers.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100


class Button:
    def __init__(self, name_button, x, y, w=50, h=100, color_fon='#ff0000', text="", color_txt='#00ff00', sh=0):
        self.pos = self.x, self.y = x, y
        self.name = name_button
        self.color_fon = color_fon
        self.color_txt = color_txt
        self.size = self.h, self.w = h, w
        self.text = text
        self.sh = sh

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_fon, (self.x, self.y, self.w, self.h), 0)
        if self.sh:
            font = pygame.font.Font(None, self.sh)
            text = font.render(self.text, True, self.color_txt)
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (self.x + abs(self.w - text_w) // 2, self.y + abs(self.h - text_h) // 2))

    def check_click(self, x, y):
        return (self.x <= x <= self.x + self.h) and (self.y <= y <= self.y + self.w)

    def change_text(self, text, color_txt, sh):
        self.text, self.color_txt, self.sh = text, color_txt, sh


class Board:
    def __init__(self, width, height, csz=70, left=10, top=10):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = csz
        self.left = left
        self.top = top

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, '#ffffff',
                                 (
                                     self.left + i * self.cell_size, self.top + j * self.cell_size,
                                     self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x < self.left or y < self.top \
                or x > self.cell_size * self.height + self.left \
                or y > self.cell_size * self.width + self.top:
            return
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        return x, y

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[x][y] == 1:
            self.board[x][y] = 2
        else:
            self.board[x][y] = 1

    def get_click(self, mouse_pos):
        coords = self.get_cell(mouse_pos)
        if coords:
            x, y = coords
        else:
            return
        self.on_click((x, y))


def draw_buttons(mas, screen):
    for i in range(len(mas)):
        mas[i].draw(screen)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    running = True
    x = y = 0
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    buttons = []
    board = Board(9, 18, 70, 10, 80)
    # buttons.append(Button('play', 300, 300, 200, 100, 'blue', 'Play', 'red', 30))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x = max(0, x - 1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x = min(width, x + 1)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y = max(0, y - 1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y = min(height, y + 1)
        screen.fill('black')
        clock.tick(60)
        draw_buttons(buttons, screen)
        board.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
