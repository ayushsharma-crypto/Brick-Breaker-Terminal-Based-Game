from random import randint
from colorama import Back,Style
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
        if(self.point.x <= 1):
            return False
        
        final_posx = self.point.x - PADDLESTEPX
        if(self.point.x <= PADDLESTEPX):
            final_posx = 1
        new_point = Point(
            final_posx,
            self.point.y
        )
        self.frame.restore_frame(new_point,self.shape,self.dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        return True
        
    

    def move_right(self):
        '''
        Logic for moving paddle right
        '''
        if(self.point.x + self.dimension.width >= FRAMEWIDTH-1):
            return False
        
        final_pos = self.point.x + PADDLESTEPX
        if(self.point.x + self.dimension.width >= FRAMEWIDTH-PADDLESTEPX-1):
            final_pos = FRAMEWIDTH-1-self.dimension.width

        new_point = Point(
            final_pos,
            self.point.y
        )
        self.frame.restore_frame(new_point,self.shape,self.dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        return True