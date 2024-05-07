import math
import pygame


def moving_circle(screen, col: tuple, c: int, d: int):
    """Function draws the moving circle and returns positions"""
    radius = d * 3/8
    x_pos = screen.get_width()/2 + radius * math.cos(math.radians(c)) - d/8
    y_pos = screen.get_height()/2 + radius * math.sin(math.radians(c)) - d/8

    pygame.draw.ellipse(screen, col, [x_pos, y_pos, d/4-4, d/4-4], width=0)

    return x_pos, y_pos
