import pygame, random
from pygame.locals import * #From Pygame import all locals
UP=0
RIGHT=1
DOWN=2
LEFT=3
pygame.init()# init pygame game
screen = d=pygame.display.set_mode((600,600))#Screen Size display
pygame.display.set_caption('Snake Game')#Window name display
snake=[(200,200),(210,200),(220,200)]#A list with 3 tuples, each one is a spawn part of the snake.
snake_skin=pygame.Surface((10,10))#Fills the snake with 10px in x and y axis (1 Square)
snake_skin.fill((255,255,255))#Snake color
apple_pos=(random.randint(0,590), random.randint(0,590))#Set apple position on the screen randomly with 'random' module, between 0 and 590 (last possible position without get off the screen)
apple=pygame.Surface((10,10))#Fills the apple with 10px in x and y axis (1 Square)
apple.fill((255,0,0))#Apple color
my_direction=LEFT #Always at the beginning, the snake'll go to the left
while True: #Infinite loop
    for event in pygame.event.get():#Get the change events
        if event.type == QUIT:#When the user close the game
            pygame.quit()#Quit of the game
    if my_direction == UP:
        snake[0]=(snake[0][0], snake[0][1]-10)
    if my_direction == DOWN:
        snake[0]=(snake[0][0], snake[0][1]+10)
    if my_direction == RIGHT:
        snake[0]=(snake[0][0]+10, snake[0][1])
    if my_direction == LEFT:
        snake[0]=(snake[0][0]-10, snake[0][1])
    for i in range(len(snake)-1,0,-1):
        snake[i]=(snake[i-1][0],snake[i-1][1])
    screen.fill((0,0,0))#Update screen / clean screen
    screen.blit(apple, apple_pos)#Gets the apple and its position
    for pos in snake:#For each position in the snake
        screen.blit(snake_skin,pos)#Gets the 'snake_skin' variable and its position
    pygame.display.update()