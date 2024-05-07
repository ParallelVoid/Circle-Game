import pygame


def static_cirlce(screen, col: tuple, d: int):
    """Draws Static Circle"""
    pygame.draw.ellipse(screen, col, [screen.get_width()/2-d/2,
                                      screen.get_height()/2-d/2, d, d], 0)
