"""
Payton Stearns
tutorial3.py
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.1
# custom attributes
ball.dir = 1
ball.go = True

def reverse(b):
    b.dir *= -1

# Set up function for handling screen refresh
def step():
    if ball.go:
        ball.x += ball.dir
        if ball.x + ball.width > SCREEN_WIDTH or ball.x < 0:
            ball.x -= ball.dir
            reverse(ball)

# Handle the space key
def spaceKey(event):
    ball.go = not ball.go

# Handle the "reverse" key
def reverseKey(event):
    reverse(ball)

# Handle the mouse click
def mouseClick(event):
    ball.x = event.x
    ball.y = event.y

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)
myapp.run(step)