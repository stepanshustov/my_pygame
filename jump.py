import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Pers(pygame.sprite.Sprite):
    image = load_image("pers.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("pers.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    running = True
    pers = Pers()
    x = y = 500
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(pers)
    k = 0
    flag = 0
    tm = 0
    s = 0
    y0 = y1 = y
    a = (457, 652)
    b = (657, 652)
    while running:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flag < 2:
                    if flag == 0:
                        y0 = y
                    flag += 1
                    k = 8
        if y - k < y0 and flag:
            y -= k
            k -= 0.3
        else:
            y = y0
            flag = 0
        screen.fill((0, 50, 0))
        pygame.draw.line(screen, "red", a, b, 4)
        pers.rect.x = x
        pers.rect.y = y
        all_sprites.draw(screen)
        pygame.display.flip()
