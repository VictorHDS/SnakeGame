import pygame
from pygame.locals import * #From Pygame import all locals
pygame.init()# init pygame game
screen = d=pygame.display.set_mode((600,600))#Screen Size display
pygame.display.set_caption('Snake Gamee')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()