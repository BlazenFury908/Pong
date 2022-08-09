import sys

import pygame
from pygame.locals import *


def main():
    # Set up game window
    pygame.init()

    display = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pong')

    # Load textures
    paddle_texture = pygame.image.load('assets/paddle.png')
    ball_texture = pygame.image.load('assets/ball.png')
    separator_texture = pygame.image.load('assets/separator.png')

    # Load font
    font = pygame.font.Font('assets/font.ttf', 45)

    # Score
    score_l = 0
    score_r = 0

    # Positions
    player_y = 480 / 2
    opponent_y = 0

    ball_x = 640 / 2 - 16
    ball_y = 480 / 2 - 16

    # Velocity
    ball_x_velocity = 0.05
    ball_y_velocity = 0.05

    while True:
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Listens for player movement
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if player_y > 0:
                player_y = player_y - 0.1
        if pressed[pygame.K_DOWN]:
            if player_y < 480 - 64:
                player_y = player_y + 0.1

        # Roof and floor reflection
        if (ball_y >= 480 - 16) | (ball_y <= 0):
            ball_y_velocity = -ball_y_velocity

        # Paddle reflection
        if ball_x >= 640 - 32:
            ball_x_velocity = -ball_x_velocity
        else:
            if (ball_x <= 16) & ((ball_y >= player_y) & (ball_y <= player_y + 64)):
                ball_x_velocity = -ball_x_velocity

        # Checking for win
        if (ball_x < 8) | (ball_x > 640 - 8):
            if ball_x < 8:
                score_l = score_l + 1
            if ball_x > 640 - 8:
                score_r = score_r + 1

            # Resets game
            player_y = 480 / 2

            ball_x = 640 / 2 - 16
            ball_y = 480 / 2 - 16

            ball_x_velocity = 0.05
            ball_y_velocity = 0.05

        # Opponent location
        if (ball_y > 480 - 32) | (ball_y < 32):
            if ball_y > 480 - 32:
                opponent_y == 480 - 32
            if ball_y < 32:
                opponent_y == 0
        else:
            opponent_y = ball_y - 32

        # Moves ball
        ball_x = ball_x + ball_x_velocity
        ball_y = ball_y + ball_y_velocity

        display.blit((font.render(str(score_l), True, (255, 255, 255))), (125, 480 / 2 - 100))
        display.blit((font.render(str(score_r), True, (255, 255, 255))), (620 - 125, 480 / 2 - 100))

        # Paints textures
        display.blit(separator_texture, (640 / 2 - 8, 0))

        display.blit(ball_texture, (ball_x, ball_y))

        display.blit(paddle_texture, (0, player_y))
        display.blit(paddle_texture, (640 - 16, opponent_y))

        # Updates game window
        pygame.display.update()


main()
