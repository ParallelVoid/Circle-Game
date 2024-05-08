import random
import pygame
from pygame.locals import *
from draw_point_line import draw_point_line
from moving_circle import moving_circle
from static_circle import static_cirlce


# screen = pygame.display.set_mode((64, 64))
# pygame.display.set_caption('Swimmy Fish')
x = 700
y = 500

def main():
    """Main Function"""
    pygame.init()

    move = 90
    dir = 1
    score = 0
    size = (x, y)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Circle Game")
    font = pygame.font.SysFont(None, 64)

    point = random.randint(0, 360)
    carry_on = True
    clock = pygame.time.Clock()
    was_in_range = False
    in_range = False
    key = ''

    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                key=pygame.key.name(event.key)
            if event.type == pygame.QUIT:
                carry_on = False
        screen.fill((255, 255, 255))

        img = font.render("Score: " + str(score), True, (255, 0, 255))
        screen.blit(img, (40, 40))

        if screen.get_height() < screen.get_width():
            diam = 2*screen.get_height()/3

        else:
            diam = 2*screen.get_width()/3

        if key == "escape":
            carry_on = False

        static_cirlce(screen, (0, 0, 0), diam)
        static_cirlce(screen, (0, 255, 0), diam/2)

        if move == 360:
            move = 0

        player_pos = moving_circle(screen, (255, 0, 255), move, diam)
        if draw_point_line(screen, point, diam/2, diam/4, player_pos[0], player_pos[1], x, y):
            was_in_range = True
            in_range = was_in_range
            if key == 'space':
                score += 1
                prev = point
                in_range = False
                while (prev - 45) <= point <= 45 + prev:
                    point = random.randint(0, 360)
                dir *= -1
                if dir < 0:
                    dir += -.25
                else:
                    dir += .25

        if not was_in_range and key == 'space':
            carry_on = False
        if in_range and not was_in_range:
            carry_on = False
        was_in_range = False
        key = ''

        pygame.display.flip()
        clock.tick(60)
        move += dir*1
    print(score)
    pygame.quit()


if __name__ == "__main__":
    main()
