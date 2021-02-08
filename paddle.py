from random import randint
from colorama import Fore,Back,Style
from constants import FRAMEHEIGHT,FRAMEWIDTH,PADDLEHEIGHT,PADDLEWIDTH,Point,Dimension

class Paddle:
    def __init__(self,frame):
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
        '''How to render on board'''
        self.frame.update_frame(self.point, self.shape, self.dimension)
    
    def move_left(self):
        '''
        Logic for moving paddle left
        '''
        print("hi1")
        
    def move_right(self):
        '''
        Logic for moving paddle left
        '''
        print("hi2")