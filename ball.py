from random import randint
from constants import *
from colorama import Fore,Style



class Ball:

    def __init__(self,frame,paddle):
        '''
        constructor of the ball
        '''
        self.frame = frame
        self.paddle = paddle
        self.speedx = BALLSPEEDX
        self.speedy = BALLSPEEDY
        self.stick = True
        self.dimension = Dimension(3,1)
        self.point = Point(
            randint(paddle.point.x,paddle.point.x+paddle.dimension.width-self.dimension.width),
            paddle.point.y-self.dimension.height
        )
        self.shape = self.initial_shape()
        self.paddle_offset = self.point.x - self.paddle.point.x
        self.draw()



    def initial_shape(self):
        '''
        initial shape of the ball
        '''
        shape = [
            [
                f"{Fore.GREEN}{Style.BRIGHT}({Style.RESET_ALL}",
                f"{Fore.GREEN}{Style.BRIGHT}@{Style.RESET_ALL}",
                f"{Style.BRIGHT}{Fore.GREEN}){Style.RESET_ALL}"
            ],
        ]
        return shape    



    def draw(self):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)



    def flip_stick(self):
        '''
        The is function will flip the stickyness of ball
        to the paddle. If self.stick is True, ball will be
        attached to the paddle. Otherwise not.
        '''
        if self.stick:
            self.stick = False
        else:
            self.stick = True
    


    def move_with_paddle(self):
        '''
        Logic for moving ball with paddle horizontally when stick.
        '''
        if not self.stick:
            return False
        
        new_point = Point(
            self.paddle.point.x + self.paddle_offset,
            self.point.y
        )

        self.frame.restore_frame(new_point,self.shape,self.dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        return True