import pygame
from pygame.draw import *

pygame.init()

# make an variable for determing frames per second of the screen
FPS = 30

pygame.display.set_caption("Angry Face")
screen = pygame.display.set_mode((400, 400))
screen.fill((150, 150, 150))

# draw the biggest yellow circle for face
circle(screen, (240, 233, 13), (200, 200), 100)
# draw a black line around it
circle(screen, (0, 0, 0), (200, 200), 100, 2)
# draw a rectangle for mouth
rect(screen, (0, 0, 0), (150, 250, 100, 20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()