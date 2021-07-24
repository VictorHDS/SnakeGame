import pygame, random
from pygame.locals import * #From Pygame import all locals
#Note: 10px = 1 Square
def on_grid_random():
    #Generates randowmly the apple on the x, y axis of the grid between 0 and 590
    x=random.randint(0,590)
    y=random.randint(0,590)
    #It performs an integer division by 10, so even if there's a fragmented number in that division, that number will revert a multiple of 10 when multiplying by 10
    return(x//10*10,y//10*10)
def collision(c1,c2):#Collision function between two distinct cells
    #There'll be collision when both 0 and 1 positions of one cell are the same as the other cell
    return (c1[0]==c2[0]) and (c1[1]==c2[1])
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
apple_pos=on_grid_random()#Get the 'on_grid_random' function
apple=pygame.Surface((10,10))#Fills the apple with 10px in x and y axis (1 Square)
apple.fill((255,0,0))#Apple color
my_direction=LEFT #Always at the beginning, the snake'll go to the left
clock=pygame.time.Clock()#Limits game FPS through the time method clock()
while True: #Infinite loop
    clock.tick(20)#Limits the FPS to 20
    for event in pygame.event.get():#Get the change events
        if event.type == QUIT:#When the user close the game
            pygame.quit()#Quit of the game
        if event.type == KEYDOWN:#If there're event changes through the keyboard
            if event.key == K_UP:#If the 'up' key is pressed
                my_direction = UP#Then my direction is up
            if event.key == K_DOWN:#If the 'down' key is pressed
                my_direction = DOWN#Then my direction is down
            if event.key == K_LEFT:#If the 'left' key is pressed
                my_direction = LEFT#Then my direction is left
            if event.key == K_RIGHT:#If the 'right' key is pressed
                my_direction = RIGHT#Then my direction is right
    if collision(snake[0],apple_pos):#If there's a collision between the snake's head and the apple's position
        apple_pos = on_grid_random()#The apple'll be generated once again randomly in the grid
        snake.append((0,0))#Adds +1 square to snake size
    #Each position of the snake's body will occupy the position that the front body was occupying
    for i in range(len(snake)-1,0,-1):#The tail'll occupy the previous position
        snake[i]=(snake[i-1][0],snake[i-1][1])

    if my_direction == UP:#If my direction goes up
        snake[0]=(snake[0][0], snake[0][1]-10)#Decrease the 'y' by 10px (1 Square)
    if my_direction == DOWN:#If my direction goes down
        snake[0]=(snake[0][0], snake[0][1]+10)#Increase the 'y' by 10px (1 Square)
    if my_direction == RIGHT:#If my direction goes right
        snake[0]=(snake[0][0]+10, snake[0][1])#Increase the 'x' by 10px (1 Square)
    if my_direction == LEFT:#If my direction goes left
        snake[0]=(snake[0][0]-10, snake[0][1])#Decrease the 'x' by 10px (1 Square)
    
    screen.fill((0,0,0))#Update screen / clean screen
    screen.blit(apple, apple_pos)#Gets the apple and its position
    for pos in snake:#For each position in the snake
        screen.blit(snake_skin,pos)#Gets the 'snake_skin' variable and its position
    pygame.display.update()