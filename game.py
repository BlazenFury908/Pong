import sys

import pygame as pg
from pygame import QUIT

from player import Player
from ball import Ball
from opponent import Opponent

from score import Score


class Game:

    def __init__(self):
        self.opponent = None
        self.ball = None
        self.player = None
        pg.init()

        self.display = pg.display.set_mode((640, 480))
        pg.display.set_caption('Pong')

        self.reset()

        self.score = Score(self.display)

        self.update()

    def update(self):
        separator_texture = pg.image.load('assets/separator.png')

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            self.display.fill((0, 0, 0))

            self.display.blit(separator_texture, (640 / 2 - 4, 0))

            self.player.update()
            self.ball.update(self.player.y, self.opponent.y)
            self.opponent.update(self.ball.y)

            self.score.update(self)

            pg.display.update()

    def reset(self):
        self.player = Player(self.display)
        self.ball = Ball(self.display)
        self.opponent = Opponent(self.display)
