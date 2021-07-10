import curses

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


while True: # Endless loop
    event = win.getch() # Get next character
    for c in snake:
        win.addch(c[0], c[1], '*')
    win.addch(food[0], food[1], '#')
curses.endwin() # Destroys window
print(f'Final score = {score}') # Print the value of 'score' variable on the screen