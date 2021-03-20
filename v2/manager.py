from constants import MAXSTAGE,ENEMYHEALTH, PADDLEHEALTH
from brick_layout import select_layout
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
        self.only_once = True
        self.frame = Frame(self.game_status)
        self.paddle = Paddle(self.frame)
        if self.game_status.get_stage()<MAXSTAGE:
            self.brick_layout = select_layout(self.game_status.get_stage(),self.frame,self.paddle)
            self.ball = Ball(self.frame,self.paddle,self.brick_layout,-1)
        else:
            self.brick_layout, self.ufo = select_layout(self.game_status.get_stage(),self.frame,self.paddle)
            self.ball = Ball(self.frame,self.paddle,self.brick_layout,self.ufo)

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
            if (self.game_status.get_stage()==MAXSTAGE):
                self.ufo.release_bomb()
                print("UFO HEALTH = ",self.ufo.health,"/",ENEMYHEALTH)
                if (self.only_once) and (self.ufo.health< 3):
                    self.brick_layout.__init__(self.frame)
                    self.only_once = False
        self.ball.self_move()
        self.user_input()
        self.brick_layout.change_rainbow_brick_color()
        self.brick_layout.refresh_layout()
        if (self.game_status.get_stage()==MAXSTAGE):
            self.ufo.draw()
            for bomb in self.ufo.bomb:
                bomb.draw()
        self.ball.float_power_up()
        if (self.game_status.get_stage()<MAXSTAGE) and (self.brick_layout.get_total_brick()==0):
            self.game_status.stage_up()
        else:
            pass



    def user_input(self):
        '''
        Getting input from the user for paddle movement
        '''
        ch = Get()
        ch1 = input_to(ch,self.ball.skip_iteration_tp)
   
        if ch1 == 'a' or ch1 == 'A':
            self.paddle.move_left()
            self.ball.move_with_paddle()
            if self.game_status.get_stage()==MAXSTAGE:
                self.ufo.move_with_paddle()
        elif ch1 == 'd' or ch1 == 'D':
            self.paddle.move_right()
            self.ball.move_with_paddle()
            if self.game_status.get_stage()==MAXSTAGE:
                self.ufo.move_with_paddle()
        elif ch1 == 'q' or ch1 =='Q':
            quit()
        elif ch1 == 'p' or ch1 =='P':
            self.ball.next_shape()
        # elif ch1 == 'i' or ch1 =='I':
        #     self.ball.speedx ==2
        #     self.ball.speedy ==2
        # elif ch1 == 'k' or ch1 =='K':
        #     self.ball.speedx ==1
            # self.ball.speedy ==1
        # elif ch1 == 'c' or ch1=='C':
        #     self.ball.expand_paddle_effect()
        # elif ch1 == 'v' or ch1=='V':
        #     self.ball.shrink_paddle_effect()
        # elif ch1 == 'b' or ch1=='B':
        #     self.ball.default_paddle_effect()
        elif ch1== ' ':
            self.ball.flip_stick(False)
        elif ch1 == '\\':
            self.game_status.stage_up()