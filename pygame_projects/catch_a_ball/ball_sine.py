import random
import math
import pygame


class BallSine():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # radius of ball
        self.radius = random.randint(5, 10)
        # start points of sine function
        self.x_start_sine = 0
        self.y_start_sine = 0
        # rotation angle of sine function
        self.angle = 0
        # coordinates where to move rotated sine function
        self.x_rotated_start_sine = 0
        self.y_rotated_start_sine = 0
        # init point for choosing random location
        self.random_point = 0
        self.orig_sine_angle = 0
        self.color = tuple(random.randint(0, 255) for i in range(3))
# move ball with sine interpolation and draw it on surface
# angle_inc - amount of radians per tick, changes moving smoothness of ball
# amp_multiplyer - changes amplitude of sine function
# x_inc - changes period of sine function
    def move_sin(self, angle_inc = 12, amp_multiplyer = 5, x_inc = 1):
# randomly choose one of 4 points to place sine function
        if self.random_point == 0:
            self.random_point = random.randint(1, 4)
            if self.random_point == 1:
                self.random_point = 1
                self.x_rotated_start_sine = self.screen.get_width()/2
                self.y_rotated_start_sine = 0 - (self.radius * 10)
                self.angle = random.randint(30, 90) * math.pi/180
                self.x_start_sine, self.y_start_sine = (0, 0)
            elif self.random_point == 2:
                self.random_point = 2
                self.x_rotated_start_sine = self.screen.get_width() + (self.radius * 10)
                self.y_rotated_start_sine = self.screen.get_height()/2
                self.angle = random.randint(120, 180) * math.pi/180
                self.x_start_sine, self.y_start_sine = (0, 0)
            elif self.random_point == 3:
                self.random_point = 3
                self.x_rotated_start_sine = self.screen.get_width()/2
                self.y_rotated_start_sine = self.screen.get_height() + (self.radius * 10)
                self.angle = random.randint(210, 270) * math.pi/180
                self.x_start_sine, self.y_start_sine = (0, 0)
            elif self.random_point == 4:
                self.random_point = 4
                self.x_rotated_start_sine = 0 - (self.radius * 10)
                self.y_rotated_start_sine = self.screen.get_height()/2
                self.angle = random.randint(300, 360) * math.pi/180
                self.x_start_sine, self.y_start_sine = (0, 0)


# calculate y = sin(x) function to get a point
        y_inc = math.sin(self.orig_sine_angle * (math.pi/180)) * amp_multiplyer
        self.orig_sine_angle += angle_inc
        self.x_start_sine += x_inc
        self.y_start_sine += y_inc


# rotate points by angle and move to a needed location
        x_point_rotated = (self.x_start_sine * math.cos(self.angle) + self.y_start_sine * -1 * math.sin(self.angle)) + self.x_rotated_start_sine
        y_point_rotated = (self.x_start_sine * math.sin(self.angle) + self.y_start_sine * math.cos(self.angle)) + self.y_rotated_start_sine

# checks if ball goes beyond screen space
        if (x_point_rotated > self.screen.get_width() + (self.radius * 10)) \
        or (x_point_rotated < (0 - self.radius * 10)) \
        or (y_point_rotated > (self.screen.get_height() + (self.radius * 10))) \
        or (y_point_rotated < (0 - self.radius * 10)):
            self.random_point = 0
            self.radius = random.randint(5, 10)
            self.color = tuple(random.randint(0, 255) for i in range(3))

        pygame.draw.circle(self.screen, self.color, (x_point_rotated, y_point_rotated), self.radius)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x_start_sine, self.y_start_sine), self.radius)
