from random import randint
from colorama import Fore,Back,Style
from constants import PADDLESTEPX,FRAMEHEIGHT,FRAMEWIDTH,PADDLEHEIGHT,PADDLEWIDTH,Point,Dimension

class Paddle:
    def __init__(self,frame):
        self.paddlestepx = PADDLESTEPX
        self.frame = frame
        self.shape = self.initial_shape(PADDLEWIDTH,PADDLEHEIGHT)
        self.dimension = Dimension(PADDLEWIDTH,PADDLEHEIGHT)
        self.point = Point(
            randint(10, FRAMEWIDTH-2*PADDLEWIDTH), 
            randint(FRAMEHEIGHT-5,FRAMEHEIGHT-5)
            )
        self.draw()
    
    def initial_shape(self,width,height):
        shape =  [ [ "" for i in range(width) ] for j in range(height) ]
        for h in range(height):
            for w in range(width):
                shape[h][w] = f"{Back.BLUE}{Style.BRIGHT} {Style.RESET_ALL}"
        return shape
    
    def draw(self):
        '''
        Render paddle on the base Frame
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)
    
    def move_left(self):
        '''
        Logic for moving paddle left
        '''
        if(self.point.x <= 2):
            return False
        new_point = Point(
            self.point.x - PADDLESTEPX,
            self.point.y
        )
        self.frame.restore_frame(new_point,self.shape,self.dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        return True
        
    
    def move_right(self):
        '''
        Logic for moving paddle right
        '''
        if(self.point.x + self.dimension.width >= FRAMEWIDTH-2):
            return False
        new_point = Point(
            self.point.x + PADDLESTEPX,
            self.point.y
        )
        self.frame.restore_frame(new_point,self.shape,self.dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        return True