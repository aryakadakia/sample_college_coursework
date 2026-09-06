from cs1lib import *
from random import *

# constants
BALL_RADIUS = 8
PADDLE_MOVEMENT = 5
# velocity for x and y coordinates
vx = 4
vy = -1

# Boolean values
left_up = False
left_down = False
right_up = False
right_down = False
quit = False
reset = False
# x and y coordinates for left paddle, right paddle, and ball
left_x = 0
left_y = 0
right_x = 380
right_y = 320
ball_x = 200
ball_y = 200

img1 = load_image("jojo.png")
img2 = load_image("diavolo.png")
img3 = load_image("background.png")
img4 = load_image("brooch.png")
img5 = load_image("joseph.png")

# key press functions
def keypress(key):
    global left_up, left_down, right_up, right_down, quit, reset, left_y, right_y, ball_x, ball_y

    if key == 'a':
        left_up = True
    if key == 'z':
        left_down = True
    if key == 'k':
        right_up = True
    if key == 'm':
        right_down = True
    if key == 'q':
        quit = True
    if key == ' ':
        reset = True

    if reset:
        left_y = 0
        right_y = 320
        ball_x = 200
        ball_y = 200
        reset = False

    if quit:
        cs1_quit()

# key release functions
def keyrelease(key):
    global left_up, left_down, right_up, right_down
    if key == 'a':
        left_up = False
    if key == 'z':
        left_down = False
    if key == 'k':
        right_up = False
    if key == 'm':
        right_down = False


# background, ball, and paddles functions
def background():
    draw_image(img3,0,0)


def ball():
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_fill_color(1, 1, 1)
    draw_circle(ball_x, ball_y, BALL_RADIUS)
    draw_image(img4, ball_x-8, ball_y-8)

def paddles():
    set_fill_color(1, 1, 1)
    set_stroke_width(3)
    draw_rectangle(left_x,left_y, 20, 80)
    draw_rectangle(right_x, right_y,20,80)
    draw_image(img1, left_x, left_y)
    draw_image(img2, right_x, right_y)


# main game function
def game():
    global ball_x, ball_y, vx, vy, BALL_RADIUS, left_x, left_y, right_x, right_y, PADDLE_MOVEMENT

    background()
    ball()
    paddles()

    # paddle movements
    if left_up:
        left_y = left_y - PADDLE_MOVEMENT
        if left_y <= 0:
            left_y = 0
    if left_down:
        left_y = left_y + PADDLE_MOVEMENT
        if left_y >= 320:
            left_y = 320
    if right_up:
        right_y = right_y - PADDLE_MOVEMENT
        if right_y <= 0:
            right_y = 0
    if right_down:
        right_y = right_y + PADDLE_MOVEMENT
        if right_y >= 320:
            right_y = 320

    # ball movement after contact with walls
    next_y = ball_y + vy
    if next_y - BALL_RADIUS <= 0 or next_y + BALL_RADIUS >= 400:
        vy = -vy
    next_x = ball_x + vx
    if next_x - BALL_RADIUS < 0 or next_x + BALL_RADIUS > 400:
        enable_stroke()
        set_stroke_color(0 , 0, 0)
        set_font_size(20)
        draw_text("Contact!", 150, 100)
        draw_image(img5, 100,150)

    # ball bouncing off paddles
    if left_y < next_y < (left_y + 80) and next_x == left_x+20:
        vx = -vx
        for i in range(-2, 2):     # unpredictable bouncing of paddle
            vy = vy + i
    if right_y < next_y < (right_y + 80) and next_x == right_x:
        vx = -vx
        for i in range(-2, 2):      # unpredictable bouncing of paddle
            vy = vy + i

    # ball movement
    ball_x = ball_x + vx
    ball_y = ball_y + vy

start_graphics(game, 2400, key_press=keypress, key_release=keyrelease)
