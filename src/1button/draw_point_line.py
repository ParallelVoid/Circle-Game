import math
import pygame


def draw_point_line(screen, num: int, r1: int, r2: int, x1: int, y1: int,
                    x: int, y: int):
    """Draw Line From Center"""

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

    if x1 <= middle_x <= x2 and y1 <= middle_y <= y2:
        return True
