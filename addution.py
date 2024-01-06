import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Button:
    def __init__(self, name_button, x_p: float(), y_p: float, w_p: float(), h_p: float(), width, height,
                 color_rect='#ff0000', text="",
                 color_txt='#00ff00', sh=0):
        self.x_p = x_p
        self.y_p = y_p
        self.w_p = w_p
        self.h_p = h_p
        self.pos = self.x, self.y = width * x_p, height * y_p
        self.name = name_button
        self.color_rect = color_rect
        self.color_txt = color_txt
        self.size = self.w, self.h = width * w_p, height * h_p
        self.text = text
        self.sh = sh

    def update(self, old_w, old_h, new_w, new_h):
        self.pos = self.x, self.y = new_w * self.x_p, new_h * self.y_p
        self.size = self.w, self.h = new_w * self.w_p, new_h * self.h_p
        self.sh = int(self.sh * new_w * new_h / old_h / old_w)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_rect, (self.x, self.y, self.w, self.h), 2)
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


def draw_buttons(mas, screen):
    for i in range(len(mas)):
        mas[i].draw(screen)
