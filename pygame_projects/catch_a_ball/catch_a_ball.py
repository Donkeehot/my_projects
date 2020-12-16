#!/usr/bin/env python3

from datetime import datetime
import pygame
from ball_linear import BallLinear
from ball_sine import BallSine


pygame.init()

player_name = input('Type your name here: ')
points = 0

FPS = 60
screen = pygame.display.set_mode((1200, 900))

ball_1 = BallLinear()
ball_2 = BallSine()

# determine if click is inside the ball and add point to a variable
def click(click_event, shape_x_cor, shape_y_cor, shape_radius, movement_type):
    global points
    mouse_click_x, mouse_click_y = click_event.pos
# using pythagorean theorem to calculate mouse click distance from ball shape
    mouse_click_r = ((abs(shape_x_cor - mouse_click_x))**2 + (abs(shape_y_cor - mouse_click_y)**2))**0.5
    if mouse_click_r <= shape_radius and movement_type == 'linear':
        print("HIT!")
        points += 1
        print("You have:", points, "points.")
    elif mouse_click_r <= shape_radius and movement_type == 'sin':
        print("HIT!")
        points += 5
        print("You have:", points, "points.")


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('records.txt', 'a+') as f:
                current_time = datetime.now()
                time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
                f.write(F"{player_name}           {points}           {time_string}\n")
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, ball_1.get_x_cor(), ball_1.get_y_cor(), ball_1.get_radius(), ball_1.get_movement_type())
            click(event, ball_2.get_x_cor(), ball_2.get_y_cor(), ball_2.get_radius(), ball_2.get_movement_type())
    ball_1.move_linear()
    ball_2.move_sin(x_inc=5)
    pygame.display.update()
    screen.fill((0, 0, 0))
pygame.quit()
