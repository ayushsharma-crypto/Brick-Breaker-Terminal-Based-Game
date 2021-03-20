from shooting_paddle import ShootingPaddle
from colorama.ansi import Back
from powerup import PowerUp
from brick import BRICK_TYPE_ARRAY
from paddle import Paddle
from frame import Frame
from random import Random, randint, random
import random as rm
from constants import *
from colorama import Fore,Style
import time



class Ball:
    powerupcolor = [
        f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}1{Style.RESET_ALL}",
    ]

    def __init__(self,frame: Frame,paddle: Paddle,brick_layout,ufo=-1):
        '''
        constructor of the ball
        '''
        self.ufo = ufo
        self.frame = frame
        self.paddle = paddle
        self.brick_layout = brick_layout
        self.different_types_ball = ['☻','⦾','⦿','◘','○','♥','☺']
        self.shape_index = 0
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
        self.draw()
        self.powerup = [] # all the active powerups



    def initial_shape(self):
        '''
        initial shape of the ball
        '''
        shape = [
            [
                f"{Fore.GREEN}{Style.BRIGHT}{self.different_types_ball[self.shape_index]}{Style.RESET_ALL}",
            ],
        ]
        return shape  



    def next_shape(self):
        '''
        initial shape of the ball
        '''
        self.shape_index = (self.shape_index+1)%len(self.different_types_ball)
        shape = [
            [
                f"{Fore.GREEN}{Style.BRIGHT}{self.different_types_ball[self.shape_index]}{Style.RESET_ALL}",
            ],
        ]
        self.shape = shape
        self.re_draw(self.point,self.shape,self.dimension)    



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




    def power_color(self,py,px):
        '''
        Says if the object in power up
        '''
        if (
            (self.frame.current_frame[py][px] in self.powerupcolor) or 
            ( self.frame.current_frame[py][px]==f"{Fore.GREEN}{Style.BRIGHT}|{Style.RESET_ALL}") or
            ( self.frame.current_frame[py][px]==f"{Fore.RED}{Back.WHITE}{Style.BRIGHT}o{Style.RESET_ALL}")
        ):
            return True
        return False



    def automatic_move_x(self):
        '''
        The is function will automatically move not-stick
        ball along x-axis i.e. horizontally with speed self.speedx
        and rebound after colliding with obstacle elastically
        Assume a ball of shape like `a`,`#`
        '''
        if (self.frame.current_frame[self.point.y][self.point.x-1]!=" " and 
        self.frame.current_frame[self.point.y][self.point.x+1]!=" " and
         not self.power_color(self.point.y,self.point.x-1) and
         not self.power_color(self.point.y,self.point.x+1)
         ):
            return self.point.x

        if self.direction_x==False:
            if self.frame.current_frame[self.point.y][self.point.x-1]!=" " and not self.power_color(self.point.y,self.point.x-1):
                self.catch_obstacle(self.point.x-1,self.point.y)
                self.direction_x = True
                return self.automatic_move_x()
            else:
                for i in range(1,self.speedx+1):
                    if (self.point.x-i>=0)and(self.frame.current_frame[self.point.y][self.point.x-i]!=" ") and not self.power_color(self.point.y,self.point.x-i):
                        return self.point.x-i+1
                return self.point.x-self.speedx
        
        else:
            if self.frame.current_frame[self.point.y][self.point.x+1]!=" " and not self.power_color(self.point.y,self.point.x+1):
                self.catch_obstacle(self.point.x+self.dimension.width-1+1,self.point.y)
                self.direction_x = False
                return self.automatic_move_x()
            else: 
                for i in range(1,self.speedx+1):
                    if (self.point.x+i<FRAMEWIDTH) and (self.frame.current_frame[self.point.y][self.point.x+i]!=" ") and (not self.power_color(self.point.y,self.point.x+i)):
                        return self.point.x+i-1
                return self.point.x+self.speedx




    def automatic_move_y(self):
        '''
        The is function will automatically move not-stick
        ball along y-axis i.e. vertically with speed self.speedy
        and rebound after colliding with obstacle elastically
        Assume a ball of shape like `@`,`#`
        '''
        if (self.frame.current_frame[self.point.y+1][self.point.x]!=" " and 
        self.frame.current_frame[self.point.y-1][self.point.x]!=" " and
        not self.power_color(self.point.y+1,self.point.x) and
        not self.power_color(self.point.y-1,self.point.x)
        ):
            return self.point.y

        if self.direction_y==False:
            if self.frame.current_frame[self.point.y+1][self.point.x]!=" " and  not self.power_color(self.point.y+1,self.point.x):
                self.catch_obstacle(self.point.x,self.point.y+1)
                self.direction_y = True
                return self.automatic_move_y()
            else:
                for j in range(1,self.speedy+1):
                    if self.frame.current_frame[self.point.y+j][self.point.x]!=" " and  not self.power_color(self.point.y+j,self.point.x) :
                        return self.point.y+j-1
                return self.point.y+self.speedy
        else:
            if self.frame.current_frame[self.point.y-1][self.point.x]!=" " and  not self.power_color(self.point.y-1,self.point.x):
                self.catch_obstacle(self.point.x,self.point.y-1)
                self.direction_y = False
                return self.automatic_move_y()
            else:
                for j in range(1,self.speedy+1):
                    if self.frame.current_frame[self.point.y-j][self.point.x]!=" " and  not self.power_color(self.point.y-j,self.point.x) :
                        return self.point.y-j+1
                return self.point.y-self.speedy




    def automatic_move(self):
        '''
        The is function will automatically move not-stick
        ball & rebound after colliding with obstacle elastically
        '''
        if self.stick:
            return False
        new_pos_y = self.automatic_move_y()
        new_pos_x = self.automatic_move_x()
        
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
            for pu in self.powerup:
                pu.self_move()
                pu.draw()
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
        if self.frame.current_frame[coy][cox] == self.paddle.shape[0][0]:
            self.handle_paddle_collision(cox)
        elif (self.ufo!=-1) and (self.frame.current_frame[coy][cox] == self.ufo.shape[0][0]):
            self.ufo.reduce_health()
        else:
            cell_value = self.frame.current_frame[coy][cox]
            for i in range(len(BRICK_TYPE_ARRAY)):
                if cell_value == BRICK_TYPE_ARRAY[i]:
                    bm = self.brick_layout.get_brick_matrix()
                    row_num = (coy-self.brick_layout.point.y)//(BRICKHEIGHT+1)
                    for brick in bm[row_num]:
                        if (brick.point.x<=cox) and (brick.point.x+BRICKWIDTH>cox):
                            if (i == 0):
                                brick.break_brick()
                                self.brick_layout.decrease_total_brick()
                                if (randint(1,10) <= (10*POWERUPPROB)) and (not brick.rainbow) and (self.frame.status.get_stage()<MAXSTAGE):
                                    self.powerup.append(ShootingPaddle(self,self,self.frame,self.paddle,self.brick_layout))
                            elif i == 4:
                                self.initiate_chain_reaction(row_num,brick)
                            else:
                                brick.break_brick()
                            break
                    if (self.frame.status.get_stage()<MAXSTAGE):
                        self.brick_layout.update_all_brick_location()
                    break



    def initiate_chain_reaction(self,row_num,brick):
        '''
        This function will handle the chain reaction
        in case the ball hits special bricks that is
        exploding brick.
        '''
        if self.frame.current_frame[brick.point.y][brick.point.x]==" ":
            return
        brick.break_brick()
        self.brick_layout.decrease_total_brick()
        
        left_brick = self.get_left_brick(brick,row_num)
        right_brick = self.get_right_brick(brick,row_num)
        top_brick = self.get_top_brick(brick,row_num)
        bottom_brick = self.get_bottom_brick(brick,row_num)
        left_top_brick = self.get_left_top_brick(brick,row_num)
        right_top_brick = self.get_right_top_brick(brick,row_num)
        left_bottom_brick = self.get_left_bottom_brick(brick,row_num)
        right_bottom_brick = self.get_right_bottom_brick(brick,row_num)



    def get_left_brick(self,this_brick,row_num):
        '''
        The is function will get brick left to brick with point this_brick
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x-BRICKWIDTH-1) and (y==this_point.y):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break        



    def get_right_brick(self,this_brick,row_num):
        '''
        The is function will get brick right to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x+BRICKWIDTH+1) and (y==this_point.y):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break        



    def get_top_brick(self,this_brick,row_num):
        '''
        The is function will get brick top to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if row_num==0:
            return
        row_num -= 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x) and (y==this_point.y-1-BRICKHEIGHT):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break               



    def get_bottom_brick(self,this_brick,row_num):
        '''
        The is function will get brick bottom to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if (row_num+1)==(LAYOUTHEIGHT//(BRICKHEIGHT+1)):
            return
        row_num += 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x) and (y==this_point.y+1+BRICKHEIGHT):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break



    def get_left_top_brick(self,this_brick,row_num):
        '''
        The is function will get brick left-top to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if row_num==0:
            return
        row_num -= 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x-BRICKWIDTH-1) and (y==this_point.y-1-BRICKHEIGHT):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break



    def get_right_top_brick(self,this_brick,row_num):
        '''
        The is function will get brick right-top to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if row_num==0:
            return
        row_num -= 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x+BRICKWIDTH+1) and (y==this_point.y-1-BRICKHEIGHT):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break



    def get_left_bottom_brick(self,this_brick,row_num):
        '''
        The is function will get brick left-bottom to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if (row_num+1)==(LAYOUTHEIGHT//(BRICKHEIGHT+1)):
            return
        row_num += 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x-BRICKWIDTH-1) and (y==this_point.y+BRICKHEIGHT+1):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break



    def get_right_bottom_brick(self,this_brick,row_num):
        '''
        The is function will get brick right-bottom to brick with point this_point
        '''
        bm = self.brick_layout.get_brick_matrix()
        this_point = this_brick.point
        if (row_num+1)==(LAYOUTHEIGHT//(BRICKHEIGHT+1)):
            return
        row_num += 1
        for cell in range(len(bm[row_num])):
            x,y = bm[row_num][cell].point.x,bm[row_num][cell].point.y
            if (x==this_point.x+BRICKWIDTH+1) and (y==this_point.y+1+BRICKHEIGHT):
                if self.frame.current_frame[y][x]==" ":
                    ''' Already Deleted '''
                elif self.frame.current_frame[y][x]==BRICK_TYPE_ARRAY[4]:
                    self.initiate_chain_reaction(row_num,bm[row_num][cell])
                elif self.frame.current_frame[y][x] == BRICK_TYPE_ARRAY[3]:
                    bm[row_num][cell].explode_unbreak_brick()
                else:
                    while bm[row_num][cell].break_brick_time > 0:
                        bm[row_num][cell].break_brick()
                        if bm[row_num][cell].break_brick_time == 0:
                            self.brick_layout.decrease_total_brick()
                break




    def burst(self):
        '''
        The is function will delete the ball.
        '''
        self.frame.status.add_kill()
        self.shape = [[" "," "," "]]
        for pu in self.powerup:
            pu.remove_power_up()
            pu.lost_active_power_up()
            for bullet in pu.left_bullets:
                bullet.remove_bullet()
            for bullet in pu.right_bullets:
                bullet.remove_bullet()
        self.powerup = []
        self.frame.clear_frame_area(self.paddle.point,self.paddle.dimension)
        self.paddle.__init__(self.frame)
        self.re_draw(self.point,self.shape,self.dimension)
        self.__init__(self.frame,self.paddle,self.brick_layout)
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
            self.__init__(self.frame,self.paddle,self.brick_layout)


    
    def expand_paddle_effect(self):
        '''
        This function will handle the case when shrink paddle powerup is used.
        '''
        self.paddle.expand_shape()
        if self.stick:
            self.shape = [[" "," "," "]]
            self.re_draw(self.point,self.shape,self.dimension)
            self.__init__(self.frame,self.paddle,self.brick_layout)


    
    def default_paddle_effect(self):
        '''
        This function will handle the case when shrink paddle powerup is used.
        '''
        self.paddle.default_shape()
        if self.stick:
            self.shape = [[" "," "," "]]
            self.re_draw(self.point,self.shape,self.dimension)
            self.__init__(self.frame,self.paddle,self.brick_layout)


    
    def float_power_up(self):
        '''
        This function will bring the floating effect on the power ups.
        '''
        for pu in self.powerup:
            pu.draw()