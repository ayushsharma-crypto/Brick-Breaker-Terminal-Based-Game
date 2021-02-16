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
        ch1 = input_to(ch,self.ball.skip_iteration_tp)
   
        if ch1 == 'a' or ch1 == 'A':
            self.paddle.move_left()
            self.ball.move_with_paddle()
        elif ch1 == 'd' or ch1 == 'D':
            self.paddle.move_right()
            self.ball.move_with_paddle()
        elif ch1 == 'q' or ch1 =='Q':
            quit()
        # elif ch1 == 'i' or ch1 =='I':
        #     self.ball.speedx += 1
        #     self.ball.speedy += 1
        elif ch1 == 'c' or ch1=='C':
            self.ball.expand_paddle_effect()
        elif ch1 == 'v' or ch1=='V':
            self.ball.shrink_paddle_effect()
        elif ch1 == 'b' or ch1=='B':
            self.ball.default_paddle_effect()
        elif ch1== ' ':
            self.ball.flip_stick(False)