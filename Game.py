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

pad1 = Sprite("Images/arts/Player.png")
pad1.set_position(_width - pad1.width - 5, (_height/2) - (pad1.height/2))


pad2 = Sprite("Images/arts/Computer.png")
pad2.set_position(5, (_height/2) - (pad2.height/2))


ball = Sprite("Images/arts/Ball.png") 
ball_0_Pos = ((_width / 2) - (ball.width/2) , (_height / 2) - (ball.height/2))
ball.set_position(ball_0_Pos[0], ball_0_Pos[1])



init_vel_x = 150
init_vel_y = 170

vel_x = 150
vel_y = 170

on_screen = True


p1_point = 0
p2_point = 0

pad_spd =  100
# O jogo so começa quando apertar barra de espasso
# Quanto mas tempo apertar a barra de espasso mais rapido a barra sai

bkgrond_image = Sprite("Images/arts/Board.png")

txt_offset = 10
# Game loop
while True:
    bkgrond_image.draw()
    #wind.set_background_color([0,12,24])
    clock.tick(_FPS)

    p1_img_size = (15, 10)

    wind.draw_text(str(p1_point), _width/2 - p1_img_size[0] - txt_offset, 5, 24, (255, 255, 255))
    wind.draw_text(str(p2_point), _width/2 + txt_offset, 5, 24, (255, 255, 255))

    
    # Condição de vitoria
    if  0 >= ball.x:
        p1_point += 1
        init_vel_x = vel_x
        init_vel_y = vel_y
        vel_x = 0
        vel_y = 0
        ball.set_position(ball_0_Pos[0], ball_0_Pos[1])
    elif ball.x >= _width - ball.width:
        p2_point += 1
        init_vel_x = vel_x
        init_vel_y = vel_y
        vel_x = 0
        vel_y = 0
        ball.set_position(ball_0_Pos[0], ball_0_Pos[1])
    # Ball Update

    ## Update x
    if ball.collided(pad1):
        vel_x *= -1
        ball.set_position(pad1.x - (ball.width) , ball.y)
    if ball.collided(pad2):
        vel_x *= -1
        ball.set_position(pad2.x + pad2.width, ball.y)
        
    ## Update y
    if  0 > ball.y:
        vel_y *= -1
        ball.set_position(ball.x, 0)
    elif ball.y > _height - ball.height:
        vel_y *= -1
        ball.set_position(ball.x, _height - ball.height)

    ## Ball new position
    ball.x += vel_x * wind.delta_time()
    ball.y += vel_y * wind.delta_time()
    ball.set_position(ball.x, ball.y)

    fram_distance = pad_spd * wind.delta_time()
    # Inputs
    ## P1
    if kb.key_pressed("up"): # y negativo para em 0
        pad1.move_y(-fram_distance)
        if pad1.y < 0 + _placarOffset:
            pad1.set_position(pad1.x, 0 + _placarOffset)
    if kb.key_pressed("down"): # y possitivo para em _height - pad.heght
        pad1.move_y(fram_distance)
        if pad1.y > _height - pad1.height:
            pad1.set_position(pad1.x, _height - pad1.height)

    ## P2
    if kb.key_pressed("w"): # y negativo para em 0
        pad2.move_y(-fram_distance)
        if pad2.y < 0 + _placarOffset:
            pad2.set_position(pad2.x, 0 + _placarOffset)
    if kb.key_pressed("s"): # y possitivo para em _height - pad.heght
        pad2.move_y(fram_distance)
        if pad2.y > _height - pad2.height:
            pad2.set_position(pad2.x, _height - pad2.height)

    ## Game
    if kb.key_pressed("space"):
        vel_x = init_vel_x
        vel_y = init_vel_y
    if kb.key_pressed("ESC"):
        wind.close()

    ball.draw()
    pad1.draw()
    pad2.draw()

    
    wind.update()