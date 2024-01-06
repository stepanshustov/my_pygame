import pygame
import os
from addution import *

MINWIDTH = 800
MINHEIGHT = 450

if __name__ == '__main__':
    state = "main"
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    running = True
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    buttons = list()
    buttons.append(Button("play", 0.2, 0.2, 0.1, 0.1, width, height, text="Play", sh=50))
    orig_fon = load_image('fon.jpg')
    fon = pygame.transform.scale(orig_fon, (width, height))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #
                running = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #         x = max(0, x - 1)
            #     elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #         x = min(width, x + 1)
            #     elif event.key == pygame.K_UP or event.key == pygame.K_w:
            #         y = max(0, y - 1)
            #     elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #         y = min(height, y + 1)
            if state == "main":
                if event.type == pygame.VIDEORESIZE:
                    old_size = size
                    width, height = pygame.display.get_surface().get_size()
                    width = max(width, MINWIDTH)
                    height = max(height, MINHEIGHT)
                    size = width, height
                    for el in buttons:
                        el.update(*old_size, *size)
                    fon = pygame.transform.scale(orig_fon, (width, height))
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        clock.tick(50)
        if state == "main":
            screen.blit(fon, (0, 0))
        draw_buttons(buttons, screen)
        all_sprites.draw(screen)
        pygame.display.flip()
