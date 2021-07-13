import curses
from random import randint
# Setup Window
curses.initscr() # Initialize screen
# 20 lines, 60 columns, starts at 0,0
win = curses.newwin(20, 60, 0, 0) #'y', 'x'
win.keypad(1) # Arrow keys to control the snake
curses.noecho() # We don't need input other characters
curses.curs_set(0) # Hide the cursor
win.border(0) # Draw the border
win.nodelay(1) # or -1. We don't wait user hits next key, but continue.

# Snake and Food
snake = [(4, 10), (4, 9), (4, 8)] # A list storing coordinates with tuples, because it's imutable
food = (10, 20) # Just a tuple storing the food initial coordinates

win.addch(food[0], food[1], '#') # Add the first food with the index of the coordinates

# Game Logic
score = 0 # 'score' starts at '0'

ESC = 27 # 'ESC' key is defined as 'key 27' in the 'curses' module
key = curses.KEY_RIGHT # Starts by moving the snake to the right
while key != ESC: # While the user don't press the 'ESC' key, the 'while loop' should continue
    win.addstr(0, 2, 'Score ' + str(score) + ' ') # Add the 'Score' string, plus the value of 'score' in the line 0, colunm 2
    win.timeout(150 -(len(snake)) // 5 + len(snake) //10 % 120) # Increase Speed based on the length of the snake
    
    prev_key = key # Previous key is the current key (in this case is the 'right arrow key')
    event = win.getch() # Get next character
    key = event if event != -1 else prev_key # The next key is the value of 'event', if the snake don't hit itself, else, just continue with the previous key (current key to the same direction)
    
    # If none of those keys is pressed, then...
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key # Current key is the previous key
    
    # Calculate the next coordinates
    y = snake[0][0] # Don't draw the snake in 'y' axis
    x = snake[0][1] # Draw the head of the snake in 'x' axis
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) # append 0(n)
    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # If snake runs over itself
    if snake[0] in snake[1:]: break # If the head ([0]) of the snake hits any other body part ([1:])
    if snake[0] == food: # If the head is equal 
        # Eat the food
        score += 1
        food = () # The food disapear
        while food == (): # While food is none
            food = (randint(1,18), randint(1,58)) # Then food apears once again randomly in any place on the screen
            if food in snake: # If food is in the snake, then...
                food = () # Food is none
        win.addch(food[0], food[1], '#') # Add a new '#' (food) character on the window
    else:
        # Move snake
        last = snake.pop() # Remove the last '*' of the snake
        win.addch(last[0], last[1], ' ') # Put a blank space ' ' in the last part of the snake

    win.addch(snake[0][0], snake[0][1], '*') # Draw the snake again with '*'
curses.endwin() # Destroys window
print(f'Final score = {score}') # Print the value of 'score' variable on the screen