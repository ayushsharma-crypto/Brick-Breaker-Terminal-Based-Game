import time
from arts import UFO_SHAPE
from constants import Dimension, ENEMYHEALTH, FRAMEWIDTH, Point, RELEASEBOMBTP, FRAMEHEIGHT
from random import randint
from colorama import *

class UFO:
    '''
    class for last enemy ufo
    '''
    def __init__(self,paddle,frame):
        '''
        constructor of the class
        '''
        self.paddle = paddle
        self.frame = frame
        self.point = Point(self.paddle.point.x-4,2)
        self.shape = self.initial_shape()
        self.dimension = self.get_dimension()
        self.health = ENEMYHEALTH
        self.draw()
        self.tic = time.time()
        self.bomb = []
    


    def draw(self):
        '''
        Render UFO on the base Frame
        '''
        if self.health:
            self.frame.update_frame(self.point, self.shape, self.dimension)
    


    def initial_shape(self):
        '''
        Gives UFO a shape
        '''
        actual = UFO_SHAPE.copy()
        shape = [ [ "" for i in range(len(actual[i])) ] for i in range(len(actual)) ]
        for r in range(len(actual)):
            for c in range(len(actual[r])):
                if (c==0) or (c== len(actual[r])-1) or (r==0) or (r== len(actual)-1):
                    shape[r][c] = f"{Fore.RED}{Back.RED}{Style.BRIGHT}{actual[r][c]}{Style.RESET_ALL}"
                else:
                    shape[r][c] = f"{Fore.RED}{Style.BRIGHT}{actual[r][c]}{Style.RESET_ALL}"
        return shape

    


    def get_dimension(self):
        '''
        Gets dimension of the UFO
        '''
        height = len(self.shape)
        width = -1
        for i in range(height):
            if width< len(self.shape[i]):
                width = len(self.shape[i])
        return Dimension(width,height)



    def move_with_paddle(self):
        '''
        Logic for moving ball with paddle horizontally when stick.
        '''
        if self.health<=0:
            return False

        new_point = Point(
            self.paddle.point.x-4,
            self.point.y
        )

        if (new_point.x<2) or (new_point.x+self.dimension.width>FRAMEWIDTH-2):
            return
        self.re_draw(new_point,self.shape,self.dimension)
        return True


    def re_draw(self,new_point,new_shape,new_dimension):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension



    def reduce_health(self):
        '''
        It will reduce the health
        '''
        if self.health==0:
            return
        
        self.health -= 1
        if self.health<=0:
            self.frame.clear_frame_area(self.point,self.dimension)
            self.frame.status.stage_up()


    
    def release_bomb(self):
        '''
        this methhod will cause UFO trow bomb vertically downward.
        '''
        x = time.time()
        if x-self.tic>RELEASEBOMBTP:
            self.tic = x
            self.bomb.append(Bomb(self))
        
        for bomb in self.bomb:
            bomb.movey()




class Bomb:
    '''
    class for bomb dropped by UFO
    '''
    def __init__(self,ufo):
        '''
        constructor for the class
        '''
        self.ufo = ufo
        self.point = Point(
            (self.ufo.point.x+(self.ufo.dimension.width//2)),
            self.ufo.point.y+self.ufo.dimension.height
            )
        self.dimension = Dimension(1,1)
        self.shape = [[f"{Fore.RED}{Back.WHITE}{Style.BRIGHT}o{Style.RESET_ALL}"]]
        self.blasted = False
        self.draw()


    def draw(self):
        '''
        Render Bomb on the base Frame
        '''
        if not self.blasted:
            self.ufo.frame.update_frame(self.point, self.shape, self.dimension)


    def movey(self):
        '''
        dropping of the bomb
        '''
        if self.blasted:
            return
        
        no = self.ufo.frame.current_frame[self.point.y+1][self.point.x]
        if self.point.y >= FRAMEHEIGHT-2:
            self.ufo.frame.clear_frame_area(self.point,self.dimension)
            self.blasted = True
        elif no==self.ufo.paddle.shape[0][0]:
            self.ufo.frame.clear_frame_area(self.point,self.dimension)
            self.blasted = True
            self.ufo.frame.status.add_kill()
        else:
            npoint = Point(self.point.x,self.point.y+1)
            self.ufo.frame.restore_frame(npoint,self.shape,self.dimension,self.point,self.shape,self.dimension)
            self.point = Point(self.point.x,self.point.y+1)