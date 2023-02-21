import random

import pygame


class Opponent:

    def __init__(self, display):
        self.texture = pygame.image.load('assets/paddle.png')

        self.display = display
        self.y = 0

    def update(self, ball_y):
        threshold = random.randint(32, 64)

        if ball_y < self.y - threshold:
            self.y -= 0.1
        if ball_y > self.y + threshold:
            self.y += 0.1

        self.display.blit(self.texture, (640 - 16, self.y))
