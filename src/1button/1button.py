import math
import random
import pygame
from pygame.locals import *
from static_circle import static_cirlce
from moving_circle import moving_circle
from draw_point_line import draw_point_line


# screen = pygame.display.set_mode((64, 64))
# pygame.display.set_caption('Swimmy Fish')
x = 700
y = 500

def main():
    """Main Function"""
    pygame.init()

    move = 90
    dir = 1
    size = (x, y)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Circle Game")

    point = random.randint(0, 360)
    score = 0
    carry_on = True
    clock = pygame.time.Clock()

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
        screen.fill((255, 255, 255))

        if screen.get_height() < screen.get_width():
            diam = 2*screen.get_height()/3

        else:
            diam = 2*screen.get_width()/3

        static_cirlce(screen, (0, 0, 0), diam)
        static_cirlce(screen, (0, 255, 0), diam/2)

        if move == 360:
            move = 0

        player_pos = moving_circle(screen, (255, 0, 255), move, diam)
        if draw_point_line(screen, point, diam/2, diam/4, player_pos[0], player_pos[1], x, y):
            score += 1
            prev = point
            while (prev - 40) <= point <= 40 + prev:
                point = random.randint(0, 360)
            dir *= -1

        pygame.display.flip()
        clock.tick(60)
        move += dir*1
    print(score)
    pygame.quit()


if __name__ == "__main__":
    main()
