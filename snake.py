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
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], '#')

# Game Logic
score = 0 # 'score' starts at '0'

ESC = 27
key = curses.KEY_RIGHT
while key != ESC:
    win.addstr(0, 2, 'Score' + str(score) + ' ')
    win.timeout(150 -(len(snake)) // 5 + len(snake) //10 % 120) # Increase Speed
    
    prev_key = key
    event = win.getch() # Get next character
    key = event if event != -1 else prev_key
    
    if key not in [curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key
    
    # Calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    
    snake.insert(0, (y, x)) # Append 0(n)
    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # If snake runs over itself
    if snake[0] in snake[1:]: break
    if snake[0] == food:
        # Eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # Move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')
curses.endwin() # Destroys window
print(f'Final score = {score}') # Print the value of 'score' variable on the screen