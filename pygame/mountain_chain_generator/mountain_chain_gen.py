import pygame 
import random
import math

pygame.init()


FPS = 30
WIDTH = 800
HEIGHT = 600
points = 20
randomness = 100
x_coordinates = []
x_start = 0
x_end = 800
x_increment = int(WIDTH / (points - 1))
jitter = int(((x_increment / 100) * randomness) / 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# genrating coordinates along X axis 
for i in range((points - 2)):
    x = random.randint(x_increment + (x_increment * i) - jitter, x_increment + (x_increment * i) + jitter)
    x_coordinates.append(x)


print(jitter)
x_coordinates.append(x_end)
x_coordinates.insert(0, x_start)
print(x_coordinates)

# generate coordinates along Y
y_coordinates = []
y_start = 200
y_end = 300
# calculate tgA
tg_a = abs(WIDTH / (y_start - y_end))
for i in range(points - 2):
    y_min_rand_start = (int(math.ceil(x_coordinates[i + 1] / tg_a))) + y_start
    y = random.randint(y_min_rand_start, 500)
    y_coordinates.append(y)

y_coordinates.append(y_end)
y_coordinates.insert(0, y_start)
# flip mountain
for i in range(len(y_coordinates)):
    y_coordinates[i] = HEIGHT - y_coordinates[i]


    
# make one list of coordinates
mountain_path = []
for i in range(points):
    coordinate = (x_coordinates[i], y_coordinates[i])
    mountain_path.append(coordinate)


pygame.draw.polygon(screen, (255, 255, 255), (mountain_path))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
