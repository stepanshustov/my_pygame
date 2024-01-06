import pygame
import os
import sys


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if color_key is not None:
        image = pygame.image.load(fullname).convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = pygame.image.load(fullname).convert_alpha()
    return image


def load_lev(filename):
    filename = "data/" + filename
    with open(filename, 'r') as f:
        lev_map_ = [line.strip() for line in f]
    max_width = max(map(len, lev_map_))
    return list(map(lambda x: list(x.ljust(max_width, '.')), lev_map_))


filename = input("Введите название файла: ")
try:
    lev_map = load_lev(filename)
except Exception:
    print("file not find")
    exit(0)

pygame.init()
screen_size = (len(lev_map[0] * 50), 50 * len(lev_map))
screen = pygame.display.set_mode(screen_size)
FPS = 50

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')

tile_width = tile_height = 50


class SpriteGroup(pygame.sprite.Group):
    def get_event(self, event):
        for sprite in self:
            sprite.get_event(event)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.rect = None

    def get_event(self, event):
        pass


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(Sprite):
    def __init__(self, *pos):
        x, y = pos
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * x + 15, tile_height * y + 5)
        self.pos = (x, y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


player = None
running = True
clock = pygame.time.Clock()
sprite_group = SpriteGroup()
hero_group = SpriteGroup()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается",
                  "Карта на месте"]

    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 60
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def gen_lev(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = "."
    return new_player, x, y


def move(hero, ev):
    x, y = hero.pos
    if ev == 1:
        if y > 0 and lev_map[y - 1][x] == ".":
            hero.move(x, y - 1)
    elif ev == 2:
        if y < max_y - 1 and lev_map[y + 1][x] == ".":
            hero.move(x, y + 1)
    elif ev == 3:
        if x > 0 and lev_map[y][x - 1] == ".":
            hero.move(x - 1, y)
    elif ev == 4:
        if x < max_x - 1 and lev_map[y][x + 1] == ".":
            hero.move(x + 1, y)


start_screen()

hero, max_x, max_y = gen_lev(lev_map)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(hero, 1)
            elif event.key == pygame.K_DOWN:
                move(hero, 2)
            elif event.key == pygame.K_LEFT:
                move(hero, 3)
            elif event.key == pygame.K_RIGHT:
                move(hero, 4)
            elif event.key == pygame.K_p:
                start_screen()
    screen.fill(pygame.Color("#000000"))
    sprite_group.draw(screen)
    hero_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
