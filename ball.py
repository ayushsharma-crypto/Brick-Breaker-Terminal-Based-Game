from paddle import Paddle
from frame import Frame
from random import Random, randint, random
import random as rm
from constants import *
from colorama import Fore,Style
import time



class Ball:

    def __init__(self,frame: Frame,paddle: Paddle):
        '''
        constructor of the ball
        '''
        self.frame = frame
        self.paddle = paddle
        self.stick = True
        self.speedx = BALLSTEPX
        self.speedy = BALLSTEPY
        self.skip_iteration_tp = BALLSTEPTP
        self.tic = time.time()
        self.toc = time.time()
        self.dimension = Dimension(1,1)
        self.point = Point(
            randint(self.paddle.point.x,self.paddle.point.x+self.paddle.dimension.width-self.dimension.width),
            self.paddle.point.y-self.dimension.height
        )
        self.shape = self.initial_shape()
        self.paddle_offset = self.point.x - self.paddle.point.x
        self.direction_x = bool(rm.getrandbits(1))
        self.direction_y = True
        # self.ball_type = "DEFAULT"
        self.draw()



    def initial_shape(self):
        '''
        initial shape of the ball
        '''
        shape = [
            [
                # f"{Fore.GREEN}{Style.BRIGHT}({Style.RESET_ALL}",
                f"{Fore.GREEN}{Style.BRIGHT}@{Style.RESET_ALL}",
                # f"{Style.BRIGHT}{Fore.GREEN}){Style.RESET_ALL}"
            ],
        ]
        return shape    



    def draw(self):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)



    def re_draw(self,new_point,new_shape,new_dimension):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension




    def flip_stick(self,state: bool):
        '''
        The is function will flip the stickyness of ball
        to the paddle. If self.stick is True, ball will be
        attached to the paddle. Otherwise not.
        '''
        self.stick = state
    


    def update_paddle_offset(self,new):
        '''
        Logic for updating the ball-paddle-offset
        '''
        self.paddle_offset = new
    


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
        self.re_draw(new_point,self.shape,self.dimension)
        return True




    def automatic_move_x(self):
        '''
        The is function will automatically move not-stick
        ball along x-axis i.e. horizontally with speed self.speedx
        and rebound after colliding with obstacle elastically
        Assume a ball of shape like `(a)`,`(#)`
        '''
        if self.frame.current_frame[self.point.y][self.point.x-1]!=" " and self.frame.current_frame[self.point.y][self.point.x+self.dimension.width-1+1]!=" ":
            return self.point.x

        if self.direction_x==False:
            if self.frame.current_frame[self.point.y][self.point.x-1]!=" ":
                self.direction_x = True
                self.catch_obstacle(self.point.x-1,self.point.y)
                return self.automatic_move_x()
            else:
                for i in range(1,self.speedx+1):
                    if self.frame.current_frame[self.point.y][self.point.x-i]!=" ":
                        return self.point.x-i+1
                return self.point.x-self.speedx
        
        else:
            if self.frame.current_frame[self.point.y][self.point.x+self.dimension.width-1+1]!=" ":
                self.direction_x = False
                self.catch_obstacle(self.point.x+self.dimension.width-1+1,self.point.y)
                return self.automatic_move_x()
            else: 
                for i in range(1,self.speedx+1):
                    if self.frame.current_frame[self.point.y][self.point.x+self.dimension.width-1+i]!=" ":
                        return self.point.x+i-1         
                return self.point.x+self.speedx




    def automatic_move_y(self):
        '''
        The is function will automatically move not-stick
        ball along y-axis i.e. vertically with speed self.speedy
        and rebound after colliding with obstacle elastically
        Assume a ball of shape like `(@)`,`(#)`
        '''
        for i in range(self.dimension.width):
            if self.frame.current_frame[self.point.y+1][i+self.point.x]!=" " and self.frame.current_frame[self.point.y-1][i+self.point.x]!=" ":
                return self.point.y

        if self.direction_y==False:
            step_down = FRAMEHEIGHT*2
            for i in range(self.dimension.width):
                if self.frame.current_frame[self.point.y+1][i+self.point.x]!=" ":
                    self.direction_y = True
                    self.catch_obstacle(i+self.point.x,self.point.y+1)
                    return self.automatic_move_y()
                else:
                    curr_step_down = self.speedy
                    for j in range(1,self.speedy+1):
                        if self.frame.current_frame[self.point.y+j][self.point.x+i]!=" ":
                            curr_step_down=j-1
                            break
                    if curr_step_down < step_down:   
                        step_down = curr_step_down             
        
            return self.point.y+step_down
        
        else:
            step_up = FRAMEHEIGHT*2
            for i in range(self.dimension.width):
                if self.frame.current_frame[self.point.y-1][i+self.point.x]!=" ":
                    self.direction_y = False
                    self.catch_obstacle(i+self.point.x,self.point.y-1)
                    return self.automatic_move_y()
                else:
                    curr_step_up = self.speedy
                    for j in range(1,self.speedy+1):
                        if (self.point.y-j < 1) or (self.frame.current_frame[self.point.y-j][i+self.point.x]!=" "):
                            curr_step_up = j-1
                            break
                    if curr_step_up < step_up:
                        step_up = curr_step_up

            return self.point.y-step_up




    def automatic_move(self):
        '''
        The is function will automatically move not-stick
        ball & rebound after colliding with obstacle elastically
        Assume a ball of shape like `(@)`,`(#)`
        '''
        if self.stick:
            return False
        new_pos_x = self.automatic_move_x()
        new_pos_y = self.automatic_move_y()
        
        if not new_pos_x:
            new_pos_x=self.point.x
        if not new_pos_y:
            new_pos_y=self.point.y

        if self.check_burst(new_pos_y):
            return False

        new_point = Point(new_pos_x,new_pos_y)      
        self.re_draw(new_point,self.shape,self.dimension)
        return True



    def self_move(self):
        '''
        The is function will automatically move not-stick
        ball after certain time-interval
        '''
        self.toc = time.time()
        if self.toc -self.tic >self.skip_iteration_tp:
            self.tic =self.toc
            self.automatic_move()
        else:
            pass
    


    def handle_paddle_collision(self,cox):
        '''
        The is function will make ball-paddle-collision effect
        '''
        self.update_paddle_offset(cox-self.paddle.point.x)
        paddle_len_unit = self.paddle.dimension.width/5
        if(self.paddle_offset<paddle_len_unit):
            '''
            Hit leftmost
            '''
            if self.speedx == 0:
                self.direction_x=False
                self.speedx = 2        
            elif self.direction_x:
                if self.speedx==3:
                    self.speedx=1
                elif self.speedx<=2:
                    self.speedx=0
            else:
                self.speedx = 3
        elif(self.paddle_offset<(paddle_len_unit)*2):
            '''
            Hit mid of left-end & center
            '''
            if self.speedx == 0:
                self.direction_x=False
                self.speedx = 1
            elif self.direction_x:
                if self.speedx == 3:
                    self.speedx = 2
                elif self.speedx<=2:
                    self.speedx = 1
            else:
                self.speedx = 2
        elif(self.paddle_offset<(paddle_len_unit)*3):
            '''
            Hit center - No effect in horizontal velocity
            '''
            
        elif(self.paddle_offset<(paddle_len_unit)*4):
            '''
            Hit mid of right-end & center
            '''
            if self.speedx == 0:
                self.direction_x=True
                self.speedx = 1
            elif self.direction_x:
                self.speedx = 2
            else:
                if self.speedx == 3:
                    self.speedx = 2
                elif self.speedx<=2:
                    self.speedx = 1
        else:
            '''
            Hit rightmost
            '''
            if self.speedx==0:
                self.direction_x = True
                self.speedx = 2
            elif self.direction_x:
                self.speedx = 3
            else:
                if self.speedx==3:
                    self.speedx==0
                elif self.speedx<=2:
                    self.speedx=0



    def catch_obstacle(self,cox,coy):
        '''
        The is function will print the current object
        on frame at the co-ordinate cox,coy
        '''
        # print("[",self.frame.current_frame[coy][cox],"]","cox =
        if self.frame.current_frame[coy][cox] == self.paddle.shape[0][0]:
            # print(self.speedx)
            # self.flip_stick(True)
            # print(self.speedx)
            self.handle_paddle_collision(cox)
            # print(self.speedx)
            # time.sleep(1)
            # self.flip_stick(False)
            # print(self.speedx)
            # time.sleep(2)



    def burst(self):
        '''
        The is function will delete the ball.
        '''
        self.frame.status.add_kill()
        self.shape = [[" "," "," "]]
        self.re_draw(self.point,self.shape,self.dimension)
        self.__init__(self.frame,self.paddle)
        return True



    def check_burst(self,new_pos_y):
        '''
        The is function will delete the ball if 
        hits bottom of the frame.
        Assume a ball of shape like `(@)`,`(#)`
        '''
        if new_pos_y < FRAMEHEIGHT-2:
            return False
        self.burst()
        return True


    
    def shrink_paddle_effect(self):
        '''
        This function will handle the case when shrink paddle powerup is used.
        '''
        self.paddle.shrink_shape()
        if self.stick:
            self.shape = [[" "," "," "]]
            self.re_draw(self.point,self.shape,self.dimension)
            self.__init__(self.frame,self.paddle)


    
    def expand_paddle_effect(self):
        '''
        This function will handle the case when shrink paddle powerup is used.
        '''
        self.paddle.expand_shape()
        if self.stick:
            self.shape = [[" "," "," "]]
            self.re_draw(self.point,self.shape,self.dimension)
            self.__init__(self.frame,self.paddle)


    
    def default_paddle_effect(self):
        '''
        This function will handle the case when shrink paddle powerup is used.
        '''
        self.paddle.default_shape()
        if self.stick:
            self.shape = [[" "," "," "]]
            self.re_draw(self.point,self.shape,self.dimension)
            self.__init__(self.frame,self.paddle)
