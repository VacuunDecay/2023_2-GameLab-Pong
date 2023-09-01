import math
import random as rd

from PPlay.window import *
from PPlay.sprite import *




_height = 455
_width = 802
_placarOffset = 50

rd.seed(time.time())

janela = Window(802, 455)
janela.set_title('Pong')

keyboard = janela.get_keyboard()




class Force:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def from_polar(mag, ang):
        ang_r = math.radians(ang)

        x = mag * math.cos(ang_r)
        y = mag * math.sin(ang_r)

        return Force(x, y)

    def reflect_x(self):
        self.x = -self.x
    
    def reflect_y(self):
        self.y = -self.y
    
    def rotate(self, angle_deg):
        
        #Converting the angle to radians
        angle_rad = math.radians(angle_deg)

        #Rotating the angle
        nx = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        ny = self.x * math.cos(angle_rad) + self.y * math.sin(angle_rad)

        #updating
        self.x = nx
        self.y = ny

class Ball(Sprite):
    sp = Force.from_polar(0.1, rd.randrange(-45, 45))


    def __init__(self, file, x=janela.width/2, y=janela.height/2):

        super().__init__(file)

        self.x = x
        self.y = y

        self.set_position(self.x, self.y)
    
    def move(self):
        self.move_x(self.sp.x)
        self.move_y(self.sp.y)
    
    def restart(self):
        self.set_position(janela.width/2, y=janela.height/2)

class Player(Sprite):
    sp = 0.1
    point = 0

    def __init__(self, file):
        super().__init__(file)
        self.set_position(20, _height/2 - self.height/2)
    
    def move(self):
        if self.y > _placarOffset and self.y < _height - self.height - 5:
            self.move_key_y(self.sp)
        elif self.y < _placarOffset:
            self.move_y(1)
        elif self.y > _height - self.height - 5:
            self.move_y(-1)

    def addScore(self, num = 1):
        self.point += num

class Computer(Sprite):
    sp = 0.05
    point = 0

    def __init__(self, file):
        super().__init__(file)
        self.set_position(_width - 20 - self.width, _height/2 - self.height/2)
    
    def move(self, target):
        if self.y > _placarOffset and self.y < _height - self.height - 5: # Nao sair da tela
            if target.y > self.y + self.height/2:
                self.move_y(self.sp)
            if target.y < self.y + self.height/2:
                self.move_y(-self.sp)
        elif self.y < _placarOffset: # se passar do limite voulta um pouco
            self.move_y(1)
        elif self.y > _height - self.height - 5: # se passar do limite voulta um pouco
            self.move_y(-1)

    def addScore(self, num = 1):
        self.point += num

        

player = Player("Images\\arts\Player.png")
comp = Computer("Images\\arts\Computer.png")
ball = Ball("Images\\arts\Ball.png") 

# Game loop
while True:
    janela.set_background_color([0,12,24])
    
    ball.move()
    player.move()
    comp.move(ball)

    if ball.collided(player) or ball.collided(comp):
        ball.sp.reflect_x()
        ball.sp.rotate(rd.randint(-10, 10))
        ball.move_x(ball.sp.x*10)

    if ball.y  + ball.height > _height:
        ball.sp.reflect_y()
    elif ball.y < _placarOffset:
        ball.sp.reflect_y()

    if ball.x > _width:
        player.addScore()
        ball.restart()
        print(f'comp: {comp.point} \n player: {player.point}')
    elif ball.x < 0:
        comp.addScore()
        ball.restart()
        print(f'comp: {comp.point} \nplayer: {player.point}')

    #Inputs
    if keyboard.key_pressed("ESC"):
        janela.close()
  
    ball.draw()
    player.draw()
    comp.draw()

    janela.update()