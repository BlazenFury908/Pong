import pygame


class Score:

    def __init__(self, display):
        self.font = pygame.font.Font('assets/font.ttf', 45)

        self.display = display

        self.score_l = 0
        self.score_r = 0

    def update(self, game):
        if (game.ball.x < 8) | (game.ball.x > 640 - 8):
            if game.ball.x < 8:
                self.score_l += + 1
            if game.ball.x > 640 - 8:
                self.score_r += + 1
            game.reset()

        self.display.blit((self.font.render(str(self.score_l), True, (255, 255, 255))), (125, 480 / 2 - 100))
        self.display.blit((self.font.render(str(self.score_r), True, (255, 255, 255))), (620 - 125, 480 / 2 - 100))
