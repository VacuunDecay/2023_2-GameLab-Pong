from PPlay.sprite import Sprite


class Ball(Sprite):

    def __init__(self, file):
        super().__init__(file)
        self.offset_x = self.height/2
        self.offset_y = self.width/2

    def set_position(self, x, y):
        super().set_position(x - self.offset_x, y - self.offset_y)
    
    def set_origin(self, x, y):
        if x <= self.height:
            self.offset_x = x
        else:
            self.offset_x = self.height

        if y <= self.width:
            self.offset_y = y
        else:
            self.offset_y = self.width
        