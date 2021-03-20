import time
from constants import PADDLEHEALTH
from colorama.ansi import Fore
from frame import Frame
from random import randint
from colorama import Back,Style
from constants import EXPANDPADDLE, PADDLESTEPX,FRAMEHEIGHT,FRAMEWIDTH,PADDLEHEIGHT,PADDLEWIDTH,Point,Dimension, SHRINKPADDLE



class Paddle:

    def __init__(self,frame: Frame):
        self.paddlestepx = PADDLESTEPX
        self.frame = frame
        self.shape = self.initial_shape(PADDLEWIDTH,PADDLEHEIGHT)
        self.dimension = Dimension(PADDLEWIDTH,PADDLEHEIGHT)
        self.point = Point(
            randint(10, FRAMEWIDTH-2*PADDLEWIDTH), 
            randint(FRAMEHEIGHT-5,FRAMEHEIGHT-5)
        )
        self.health = PADDLEHEALTH
        self.draw()
    


    def initial_shape(self,width,height):
        pass
        shape =  [ [ "" for i in range(width) ] for j in range(height) ]
        for h in range(height):
            for w in range(width):
                shape[h][w] = f"{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"
        return shape
    


    def shrink_shape(self):
        pass
        shape =  [ [ "" for i in range(SHRINKPADDLE) ] for j in range(PADDLEHEIGHT) ]
        for h in range(PADDLEHEIGHT):
            for w in range(SHRINKPADDLE):
                shape[h][w] = f"{Back.RED}{Style.BRIGHT} {Style.RESET_ALL}"
        
        self.re_draw(self.point,shape,Dimension(SHRINKPADDLE,PADDLEHEIGHT))
    


    def expand_shape(self):
        pass
        shape =  [ [ "" for i in range(EXPANDPADDLE) ] for j in range(PADDLEHEIGHT) ]
        for h in range(PADDLEHEIGHT):
            for w in range(EXPANDPADDLE):
                shape[h][w] = f"{Back.BLUE}{Style.BRIGHT} {Style.RESET_ALL}"
        
        self.re_draw(self.point,shape,Dimension(EXPANDPADDLE,PADDLEHEIGHT))
    


    def default_shape(self):
        pass
        shape =  [ [ "" for i in range(PADDLEWIDTH) ] for j in range(PADDLEHEIGHT) ]
        for h in range(PADDLEHEIGHT):
            for w in range(PADDLEWIDTH):
                shape[h][w] = f"{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"
        
        self.re_draw(self.point,shape,Dimension(PADDLEWIDTH,PADDLEHEIGHT))
    


    def draw(self):
        '''
        Render paddle on the base Frame
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)



    def re_draw(self,new_point,new_shape,new_dimension):
        '''
        Render paddle again on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension
    


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


        
    def add_cannon(self):
        r1 = [ self.shape[0][0] for i in range(self.dimension.width)]        
        r2 = [ " " for i in range(self.dimension.width)]        
        r2[0] = f"{Fore.GREEN}{Style.BRIGHT}^{Style.RESET_ALL}"
        r2[-1] = f"{Fore.GREEN}{Style.BRIGHT}^{Style.RESET_ALL}"
        r3 = [ " " for i in range(self.dimension.width)]        
        r3[0] = f"{Fore.GREEN}{Style.BRIGHT}^{Style.RESET_ALL}"
        r3[-1] = f"{Fore.GREEN}{Style.BRIGHT}^{Style.RESET_ALL}"
        self.shape = [r1,r2, r3]
        self.dimension = Dimension(self.dimension.width,3)
        self.draw()


        
    def remove_cannon(self):
        old_shape = self.shape
        old_d = self.dimension
        self.shape = self.initial_shape(PADDLEWIDTH,PADDLEHEIGHT)
        self.dimension = Dimension(PADDLEWIDTH,PADDLEHEIGHT)
        self.frame.restore_frame(self.point,self.shape,self.dimension,self.point,old_shape,old_d)