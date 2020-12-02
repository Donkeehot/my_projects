#!/usr/bin/env python3

import random
import pygame

class Ball():
    def __init__(self):
        self.screen = screen = pygame.display.get_surface()
        self.radius = radius = random.randint(5, 30)
        self.x_cor = x_cor = random.randint(radius, self.screen.get_width() - radius)
        self.y_cor = y_cor = random.randint(radius, self.screen.get_height() - radius)
        self.color = color = tuple(random.randrange(0, 255) for i in range(3))
        self.x_inc = x_inc = random.randint(-5, 5)
        self.y_inc = y_inc = random.randint(-5, 5)

# move ball with linear interpolation and draw it on surface
    def move_linear(self):
        if not (self.x_inc and self.y_inc):
            self.x_inc += random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            self.y_inc += random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        self.x_cor += self.x_inc
        self.y_cor += self.y_inc

# check if ball touches screen borders
        if self.x_cor >= (self.screen.get_width() - self.radius):
            self.x_cor = self.screen.get_width() - self.radius
            self.x_inc = random.randint(-5, 0)
            self.y_inc = random.randint(-5, 5)
        elif self.x_cor <= self.radius:
            self.x_cor = self.radius
            self.x_inc += random.randint(0, 5)
            self.y_inc += random.randint(-5, 5)
        elif self.y_cor <= self.radius:
            self.y_cor = self.radius
            self.y_inc += random.randint(0, 5)
            self.x_inc += random.randint(5, 5)
        elif self.y_cor >= (self.screen.get_height() - self.radius):
            self.y_cor = self.screen.get_height() - self.radius
            self.y_inc += random.randint(-5, 0)
            self.x_inc += random.randint(-5, 5)

        pygame.draw.circle(self.screen, self.color, (self.x_cor, self.y_cor), self.radius)

# move ball with spiral interpolation and draw it on surface
    def move_spiral(self):
        pass

# move ball with zigzag interpolation and draw it on surface
    def move_zigzag(self):
        pass

    def get_x_cor(self):
        return self.x_cor

    def get_y_cor(self):
        return self.y_cor

    def get_radius(self):
        return self.radius
