import pygame
from pygame.locals import * #From Pygame import all
pygame.init()
screen = d=pygame.display.set_mode((600,600))
pygame.display.set_caption('snake')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()