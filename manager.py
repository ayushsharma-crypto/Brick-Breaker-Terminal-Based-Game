from typing import IO
from frame import Frame
from paddle import Paddle
from ball import Ball
from time import time
from input import Get,input_to

class Manager:

    def __init__(self, game_status):
        '''
        construct the walls, paddle, ball and frame
        '''
        self.game_status = game_status
        self.frame = Frame(self.game_status)
        self.paddle = Paddle(self.frame)
        self.ball = Ball(self.frame,self.paddle)
        self.frame.display()

        tic = time()        
        while True:
            flag = False
            toc = time()
            if (toc - tic) >= self.ball.skip_iteration_tp:
                flag =True
                tic = toc
            self.schedular(flag)
    


    def schedular(self,flag):
        '''
        Order of execution at each iteration.
        '''
        if flag==True:
            self.frame.display()
        self.ball.self_move()
        self.user_input()



    def user_input(self):
        '''
        Getting input from the user for paddle movement
        '''
        ch = Get()
        IO_timeout = self.ball.skip_iteration_tp
        if IO_timeout!= 0.1:
            IO_timeout = 0.06
        ch1 = input_to(ch,IO_timeout)
   
        if ch1 == 'a' or ch1 == 'A':
            self.paddle.move_left()
            self.ball.move_with_paddle()
        elif ch1 == 'd' or ch1 == 'D':
            self.paddle.move_right()
            self.ball.move_with_paddle()
        elif ch1 == 'q' or ch1 =='Q':
            quit()
        elif ch1 == 'i' or ch1 =='I':
            self.ball.skip_iteration_tp -= 0.04
        elif ch1== ' ':
            self.ball.flip_stick(False)