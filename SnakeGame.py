import pygame, random
from pygame.locals import * #From Pygame import all locals
UP=0
RIGHT=1
DOWN=2
LEFT=3
pygame.init()# init pygame game
screen = d=pygame.display.set_mode((600,600))#Screen Size display
pygame.display.set_caption('Snake Game')#Window name display
snake=[(200,200),(210,200),(220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill((255,255,255))
apple_pos=(random.randint(0,590), random.randint(0,590))
apple=pygame.Surface((10,10))
apple.fill((255,0,0))
my_direction=LEFT
while True: #Infinite loop
    for event in pygame.event.get():#Get the change events
        if event.type == QUIT:#When the user close the game
            pygame.quit()#Quit of the game
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)
    pygame.display.update()