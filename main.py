import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    running = True
    x = y = -1
    image = load_image("cr.png")
    image = pygame.transform.scale(image, (100, 100))
    while running:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos

        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused() and x != -1:
            screen.blit(image, (x, y))

        pygame.display.flip()
