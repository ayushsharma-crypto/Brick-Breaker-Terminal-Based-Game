import time
from arts import UFO_SHAPE
from constants import Dimension, ENEMYHEALTH, FRAMEWIDTH, Point
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
        self.point = Point(self.paddle.point.x-4,5)
        self.shape = self.initial_shape()
        self.dimension = self.get_dimension()
        self.health = ENEMYHEALTH
        self.draw()
    


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