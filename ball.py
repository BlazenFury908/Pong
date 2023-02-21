import random

import pygame as pg


class Ball:

    def __init__(self, display):
        self.texture = pg.image.load('assets/ball.png')

        self.display = display

        self.x = 640 / 2 - 16
        self.y = 480 / 2 - 16

        self.x_velocity = 0.05
        self.y_velocity = 0.05

        velocity_modifier = random.randint(1, 3)

        if velocity_modifier == 1:
            self.x_velocity = -self.x_velocity
        if velocity_modifier == 2:
            self.y_velocity = -self.y_velocity
        if velocity_modifier == 3:
            self.x_velocity = -self.x_velocity
            self.y_velocity = -self.y_velocity

    def update(self, player_y, opponent_y):
        if (self.y >= 480 - 16) | (self.y <= 0):
            self.y_velocity = -self.y_velocity

        if (self.x >= 640 - 32) & ((self.y >= opponent_y) & (self.y <= opponent_y + 64)):
            self.x_velocity = -self.x_velocity
        if (self.x <= 16) & ((self.y >= player_y) & (self.y <= player_y + 64)):
            self.x_velocity = -self.x_velocity

        self.x += self.x_velocity
        self.y += self.y_velocity

        self.display.blit(self.texture, (self.x, self.y))
