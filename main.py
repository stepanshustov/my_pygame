import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    running = True
    fon = load_image("fon.jpg")
    x = y = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pr = pygame.key.get_pressed()

        if pr[pygame.K_LEFT]:
            x -= 2
        if pr[pygame.K_RIGHT]:
            x += 2
        if pr[pygame.K_UP]:
            y -= 2
        if pr[pygame.K_DOWN]:
            y += 2
        x %= width
        y %= height
        screen.fill((0, 0, 0))
        screen.blit(fon, (x - width, y - height))
        pygame.display.flip()
