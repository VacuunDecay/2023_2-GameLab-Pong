import math
import random as rd

from PPlay.window import *
from PPlay.sprite import *


_height = 455
_width = 802
_FPS = 60
_placarOffset = 50

rd.seed(time.time())

wind = Window(802, 455)
wind.set_title('Pong')


clock = pygame.time.Clock()
kb = wind.get_keyboard()


ball = Sprite("Images\\arts\Ball.png") 
ball.set_position((_width / 2) - (ball.width/2) , (_height / 2) - (ball.height/2) )

pos_x = ball.x
pos_y = ball.y

vel_x = 50
vel_y = 70

on_screen = True

# Game loop
while True:
    wind.set_background_color([0,12,24])
    clock.tick(_FPS)

    ball.x += vel_x * wind.delta_time()
    ball.y += vel_y * wind.delta_time()
    ball.set_position(ball.x, ball.y)

    if  0 >= ball.x:
        vel_x *= -1
        ball.set_position(0, ball.y)
    elif ball.x >= _width - ball.width:
        vel_x *= -1
        ball.set_position(ball.x, ball.y)
    if  0 >= ball.y:
        vel_y *= -1
    elif ball.y >= _height - ball.height:
        vel_y *= -1

    #Inputs
    if kb.key_pressed("ESC"):
        wind.close()

    ball.draw()
    
    wind.update()