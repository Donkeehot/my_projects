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
# draw eyeballs
circle(screen, (255, 0, 0), (150, 200), 30)
circle(screen, (255, 0, 0), (250, 200), 20)
# draw pupils
circle(screen, (0, 0, 0), (150, 200), 12)
circle(screen, (9, 0, 0), (250, 200), 8)
# ------------drawing eybrows------------
# left eyebrow
# create a surface for rotation
left_eyebrow_surface = pygame.Surface((15, 120))
# fill with color for excluding
left_eyebrow_surface.fill((255, 0, 0))
# exclude this color
left_eyebrow_surface.set_colorkey((255, 0, 0))
# draw a rectangle inside surface
rect(left_eyebrow_surface, (0, 0, 0), (0, 0, 15, 120))
# create a new rotated surface
left_eyebrow_surface = pygame.transform.rotate(left_eyebrow_surface, 70)
# draw it on parent screen
screen.blit(left_eyebrow_surface, (70, 126))
# right eyebrow
right_eyebrow_surface = pygame.Surface((15, 120))
right_eyebrow_surface.fill((255, 0, 0))
right_eyebrow_surface.set_colorkey((255, 0, 0))
rect(right_eyebrow_surface, (0, 0, 0), (0, 0, 15, 120))
right_eyebrow_surface = pygame.transform.rotate(right_eyebrow_surface, -65)
screen.blit(right_eyebrow_surface, (220, 126))
# ------------------------------------




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()