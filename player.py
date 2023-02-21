import pygame


class Player:

    def __init__(self, display):
        self.texture = pygame.image.load('assets/paddle.png')

        self.display = display
        self.y = 480 / 2

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if self.y > 0:
                self.y -= 0.1
        if pressed[pygame.K_DOWN]:
            if self.y < 480 - 64:
                self.y += 0.1

        self.display.blit(self.texture, (0, self.y))