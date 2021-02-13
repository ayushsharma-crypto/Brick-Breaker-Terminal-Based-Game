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
            if (toc - tic) >= 0.01:
                flag =True
                tic = toc
            self.schedular(flag)
    
    def schedular(self,flag):
        '''
        Order of execution at each iteration.
        '''
        if flag==True:
            self.frame.display()
        self.user_input()


    def user_input(self):
        '''
        Getting input from the user for paddle movement
        '''
        ch = Get()
        ch1 = input_to(ch)
        print(ch1)
   
        if ch1 == 'a' or ch1 == 'A':
            self.paddle.move_left()
        elif ch1 == 'd' or ch1 == 'D':
            self.paddle.move_right()
        elif ch1 == 'q' or ch1 =='Q':
            quit()
        
        self.ball.move_with_paddle()