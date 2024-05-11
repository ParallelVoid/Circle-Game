import random
import math
from array import array
import pygame
from pygame.mixer import Sound, get_init, pre_init


class Game:
    def __init__(self, x, y):
        # initialize music
        pre_init(44100, -16, 1, 1024)
        pygame.init()

        self.x = x
        self.y = y
        self.move = 90
        self.dir = 1
        self.score = 0
        self.high_score = 0
        self.pitch = 262
        self.frame_num = 0

        size = (x, y)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        # next 2 lines might not go here
        pygame.display.set_caption("Circle Game")
        self.font = pygame.font.SysFont(None, 64)

        self.point = random.randint(0, 360)
        self.run = True
        self.game_play = True
        self.clock = pygame.time.Clock()
        self.was_in_range = False
        self.in_range = False
        self.key = ''

    def game_running(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                self.key=pygame.key.name(event.key)
            if event.type == pygame.QUIT:
                self.game_play = False
                self.run = False
        self.screen.fill((255, 255, 255))
        Note(self.pitch).play(20)

        img = self.font.render("Score: " + str(self.score), True, (255, 0, 255))
        self.screen.blit(img, (40, 40))

        if self.screen.get_height() < self.screen.get_width():
            diam = 2*self.screen.get_height()/3

        else:
            diam = 2*self.screen.get_width()/3

        if self.key == "escape":
            self.game_play = False
            self.run = False

        static_cirlce(self.screen, (0, 0, 0), diam)
        static_cirlce(self.screen, (0, 255, 0), diam/2)

        if self.move == 360:
            self.move = 0

        player_pos = moving_circle(self.screen, (255, 0, 255), self.move, diam)
        if draw_point_line(self.screen, self.point, diam/2, diam/4,
                           player_pos[0], player_pos[1], self.x, self.y):
            self.was_in_range = True
            self.in_range = self.was_in_range
            if self.key == 'space':
                Note(self.pitch).stop()
                self.pitch += 15
                Note(self.pitch).play(80)
                self.score += 1
                prev = self.point
                self.in_range = False
                while (prev - 45) <= self.point <= 45 + prev:
                    self.point = random.randint(0, 360)
                self.dir *= -1
                if self.dir < 0:
                    self.dir += -.25
                else:
                    self.dir += .25

        if not self.was_in_range and self.key == 'space':
            # game over
            self.key = ''
            self.game_play = False
            pygame.event.clear(eventtype=[pygame.KEYDOWN,pygame.KEYUP])

        if self.in_range and not self.was_in_range:
            self.key = ''
            self.game_play = False
        self.was_in_range = False
        self.key = ''

        pygame.display.flip()
        self.clock.tick(60)
        self.move += self.dir

    def render_game_over(self):
        self.screen.fill((255, 255, 255))
        img1 = self.font.render("Score: " + str(self.score), True, (255, 0, 255))
        img2 = self.font.render("High Score: " + str(self.high_score), True, (255, 0, 255))
        img3 = self.font.render("Press Any Key To Play Again", True, (255, 0, 0))
        self.screen.blit(img1, (self.screen.get_width()/2 - 100, self.screen.get_height()/2))
        self.screen.blit(img2, (self.screen.get_width()/2 - 160, self.screen.get_height()/2 - 80))
        self.screen.blit(img3, (40, self.screen.get_height()/2 + 80))
        if self.key == "escape":
            # quit the game
            self.run = False
        if self.key != '' and self.key != "escape":
            # restart the game
            self.frame_num = self.frame_num + 1
            if self.frame_num < 100:
                return
            self.frame_num = 0
            self.move = 90
            self.dir = 1
            self.score = 0
            self.was_in_range = False
            self.in_range = False
            self.point = random.randint(0, 360)
            self.key = ''
            self.game_play = True
            self.pitch = 262

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.key = pygame.key.name(event.key)
                if event.type == pygame.QUIT:
                    self.run = False
            while self.game_play:
                self.game_running()

            pygame.display.flip()
            if self.score > self.high_score:
                self.high_score = self.score
            self.render_game_over()
        pygame.quit()

class Note(Sound):
    def __init__(self, frequency, volume=.01):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples


# helper functions
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
                     (point_x1, point_y1), 10)

    x2 = x1 + r2
    y2 = y1 + r2

    if x1 <= middle_x <= x2 and y1 <= middle_y <= y2:
        return True


def static_cirlce(screen, col: tuple, d: int):
    """Draws Static Circle"""
    pygame.draw.ellipse(screen, col, [screen.get_width()/2-d/2,
                                      screen.get_height()/2-d/2, d, d], 0)


def moving_circle(screen, col: tuple, c: int, d: int):
    """Function draws the moving circle and returns positions"""
    radius = d * 3/8
    x_pos = screen.get_width()/2 + radius * math.cos(math.radians(c)) - d/8
    y_pos = screen.get_height()/2 + radius * math.sin(math.radians(c)) - d/8

    pygame.draw.ellipse(screen, col, [x_pos, y_pos, d/4-4, d/4-4], width=0)

    return x_pos, y_pos


# main
if __name__ == "__main__":
    Game(700, 500).play()
