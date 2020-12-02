import pygame 
import random
import math


def mountain_chain_gen(screen, points, y_start, y_end, color, max_height = 0, randomness = 50, x_start = 0, x_end = 0):
'''
the function draws mountain with specified paramaters
'''

# set max y and x values if not provided by user
    surface = pygame.display.get_surface()
    
    if max_height == 0:
        max_height = surface.get_height()

    if x_end == 0:
        x_end = surface.get_width()

    x_coordinates = []
# calculate distance betwen points along x axis
    x_increment = int(abs(x_start - x_end) / (points - 1))
# calculate values for points random distribution
    jitter = int(((x_increment / 100) * randomness) / 2)

# genrating coordinates along X axis 
    for i in range((points - 2)):
        x_point = random.randint(x_increment + (x_increment * i) - jitter, x_increment + (x_increment * i) + jitter)
        x_coordinates.append(x_point)

    x_coordinates.append(x_end)
    x_coordinates.insert(0, x_start)

# generate coordinates along Y
    y_coordinates = []
    
# calculate tgA to calculate minimum y value at each x point
    tg_a = abs(x_end / (y_start - y_end))
    for i in range(points - 2):
        y_min_rand_start = (int(math.ceil(x_coordinates[i + 1] / tg_a))) + y_start
        y_point = random.randint(y_min_rand_start, max_height)
        y_coordinates.append(y_point)

    y_coordinates.append(y_end)
    y_coordinates.insert(0, y_start)

# flip mountain
    screen_height = surface.get_height()
    for i in range(len(y_coordinates)):
        y_coordinates[i] = screen_height - y_coordinates[i]

# make one list of coordinates
    mountain_path = []
    for i in range(points):
        coordinate = (x_coordinates[i], y_coordinates[i])
        mountain_path.append(coordinate)

    pygame.draw.polygon(screen, (color), (mountain_path))
