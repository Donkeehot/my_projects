import pygame 
import random


pygame.init()


FPS = 30
WIDTH = 800
HEIGHT = 600
points = 10
x_coordinates = []
x_start = 0
x_end = 800
x_increment = int(WIDTH / (points - 2))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

for i in range((points - 3)):
    x = random.randint(x_increment + (x_increment * i) - 10, x_increment + (x_increment * i) + 10)
    x_coordinates.append(x)


x_coordinates.append(x_end)
x_coordinates.insert(0, x_start)
print(x_coordinates)



#pygame.draw.polygon(screen, (255, 255, 255), random_path)



#print(random_path)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()