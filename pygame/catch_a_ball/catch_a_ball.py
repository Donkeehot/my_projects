#!/usr/bin/env python3
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0

# create ball in random place of screen with random parameters
def new_ball():
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

# determine if click is inside the ball and add point to a variable
def click(event):
    global points
    mouse_click_x, mouse_click_y = event.pos
    mouse_click_r = ((abs(x - mouse_click_x))**2 + (abs(y - mouse_click_y)**2))**0.5
    if mouse_click_r <= r:
        print("HIT!")
        points += 1
        print("You have:", points, "points.")
    else:
        print("Missed!")


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
