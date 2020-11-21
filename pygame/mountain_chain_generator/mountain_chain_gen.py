import pygame 
import random
import math


def mountain_chain_gen(screen, points, y_start, y_end, color, max_height = 0, randomness = 50, x_start = 0, x_end = 0):
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
        x = random.randint(x_increment + (x_increment * i) - jitter, x_increment + (x_increment * i) + jitter)
        x_coordinates.append(x)


    x_coordinates.append(x_end)
    x_coordinates.insert(0, x_start)


# generate coordinates along Y
    y_coordinates = []
    
# calculate tgA to calculate minimum y value at each x point
    tg_a = abs(x_end / (y_start - y_end))
    for i in range(points - 2):
        y_min_rand_start = (int(math.ceil(x_coordinates[i + 1] / tg_a))) + y_start
        y = random.randint(y_min_rand_start, max_height)
        y_coordinates.append(y)

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


pygame.init()


FPS = 30
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

mountain_chain_gen(screen, 20, 0, 100, (100, 100, 100))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
