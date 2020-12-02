#!/usr/bin/env python3

import pygame
from pygame.draw import *
from random import randint
from ball import Ball

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

points = 0

ball_1 = Ball()
ball_2 = Ball()

# determine if click is inside the ball and add point to a variable
def click(click_event, shape_x_cor, shape_y_cor, shape_radius):
    global points
    mouse_click_x, mouse_click_y = click_event.pos
# using pythagorean theorem to calculate mouse click distance from ball shape
    mouse_click_r = ((abs(shape_x_cor - mouse_click_x))**2 + (abs(shape_y_cor - mouse_click_y)**2))**0.5
    if mouse_click_r <= shape_radius:
        print("HIT!")
        points += 1
        print("You have:", points, "points.")


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, ball_1.get_x_cor(), ball_1.get_y_cor(), ball_1.get_radius())
            click(event, ball_2.get_x_cor(), ball_2.get_y_cor(), ball_2.get_radius())
    ball_1.move_linear()
    ball_2.move_linear()
    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()