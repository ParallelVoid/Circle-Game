import pygame
from pygame.locals import *
import math
import random

pygame.init()

# screen = pygame.display.set_mode((64, 64))
# pygame.display.set_caption('Swimmy Fish')

def static_cirlce(col: tuple, d: int):
    pygame.draw.ellipse(screen, col, [screen.get_width()/2-d/2,
                                      screen.get_height()/2-d/2, d, d], 0)


def moving_circle(col: tuple, c: int, d: int, dir: int):  #, x_pos: int, y_pos: int):
    radius = d * 3/8
    x_pos = screen.get_width()/2 + radius * math.cos(math.radians(c)) - d/8
    y_pos = screen.get_height()/2 + radius * math.sin(math.radians(c)) - d/8

    pygame.draw.ellipse(screen, col, [x_pos, y_pos, d/4-4, d/4-4], 2)

    return x_pos, y_pos


def draw_point_line(num: int, r1: int, r2: int, x1: int, y1: int):

    yadd1 = math.sin(math.radians(num)) * r1
    xadd1 = math.cos(math.radians(num)) * r1
    yadd2 = math.sin(math.radians(num)) * r2
    xadd2 = math.cos(math.radians(num)) * r2

    point_y1 = y/2 + yadd1
    point_x1 = x/2 + xadd1
    point_y2 = y/2 + yadd2
    point_x2 = x/2 + xadd2

    middle_x = (point_x1 + point_x2)/2
    middle_y = (point_y1 + point_y2)/2

    pygame.draw.line(screen, (0, 255, 0), (x/2, y/2),
                     (point_x1, point_y1))

    x2 = x1 + r2
    y2 = y1 + r2

    if (x1 <= middle_x and middle_x <= x2) and (y1 <= middle_y and middle_y <= y2):
        return True


def main(b: bool, move: int, point: int, score: int, dir: int):
    while b:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b = False
        screen.fill((255, 255, 255))

        if screen.get_height() < screen.get_width():
            diam = 2*screen.get_height()/3

        else:
            diam = 2*screen.get_width()/3

        big_circle = static_cirlce((0, 0, 0), diam)
        small_circle = static_cirlce((0, 255, 0), diam/2)

        if move == 360:
            move = 0

        player_pos = moving_circle((255, 0, 255), move, diam, dir)
        if draw_point_line(point, diam/2, diam/4, player_pos[0], player_pos[1]):
            score += 1
            prev = point
            #point = random.randint(0, 360)
            while (prev - 40) <= point <= 40 + prev:
                point = random.randint(0, 360)
            dir *= -1

        pygame.display.flip()
        clock.tick(60)
        move += dir*1
    print(score)


x = 700
y = 500
movetimes = 90
dir = 1
size = (x, y)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Circle Game")

point = random.randint(0, 360)
score = 0
carryOn = True
clock = pygame.time.Clock()
main(carryOn, movetimes, point, score, dir)

pygame.quit()
