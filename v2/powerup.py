from paddle import Paddle
import time
from colorama.ansi import Back, Fore, Style
from constants import BALLSTEPTP, Dimension, FRAMEHEIGHT, FRAMEWIDTH, PADDLEHEIGHT, POWERUPGRAVITY, POWERUPGRAVITYTP, POWERUPWIDTH, Point
from frame import Frame

POWER_UP_ARRAY = []

class PowerUp:
    '''
    A class for various power implementation.
    '''
    def __init__(self,path,ball,frame: Frame,paddle,activetime,brick_layout):
        self.brick_layout = brick_layout
        self.path_object = path
        self.ball = ball
        self.frame = frame
        self.point = path.point
        self.paddle = paddle
        self.dimension = Dimension(POWERUPWIDTH,PADDLEHEIGHT)
        self.shape = self.shape_powerup()
        self.gravity = POWERUPGRAVITY
        self.speedx = path.speedx
        self.speedy = path.speedy
        self.directionx = path.direction_x
        self.directiony = path.direction_y
        self.display = True
        self.toc = time.time()
        self.tic = time.time()
        self.gtoc = time.time()
        self.gtic = time.time()
        self.gravityTP = POWERUPGRAVITYTP
        self.skip_iteration_tp = BALLSTEPTP
        self.flag = 0
        self.active = False
        self.active_time = activetime
        self.atic = time.time()
        self.draw()

    

    def shape_powerup(self):
        '''
        Gives shape to the powerup
        '''
        shape = [ [] for i in range(self.dimension.height) ]
        for i in range(self.dimension.height):
            for j in range(self.dimension.width):
                shape[i].append(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}1{Style.RESET_ALL}")
        return shape



    def draw(self):
        '''
        Render the power on breaking a brick
        '''
        if self.display==True:
            self.frame.update_frame(self.point, self.shape, self.dimension)



    def re_draw(self,new_point,new_shape,new_dimension):
        '''
        Render powerup on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension

    
    def power_up_start(self):
        '''
        This method just made for getting override in
        child classes.
        '''
        pass
            


    def check_paddle_collision(self,new_x,new_y):
        '''
        Checks if the powerup was catched by the paddle.
        '''
        if self.frame.current_frame[new_y][new_x] == self.paddle.shape[0][0]:
            self.active = True
            self.atic = time.time()
            return True
        else:
            return False
            


    def check_lost(self,new_y):
        '''
        Checks if the powerup was not catched by the paddle.
        '''
        if new_y  >= FRAMEHEIGHT-1:
            return True
        return False
            


    def movex(self):
        '''
        The function makes the powerup moves along x-direction.
        '''
        if self.directionx == False:
            if self.point.x==1:
                self.directionx = True
                return self.point.x+1
            elif self.point.x<=self.speedx:
                return 1
            else:
                return self.point.x-self.speedx
        else:
            if self.point.x==FRAMEWIDTH-2:
                self.directionx = False
                return self.point.x-1
            elif self.point.x>=(FRAMEWIDTH-self.speedx-2):
                return FRAMEWIDTH-2
            else:
                return self.point.x+self.speedx
            


    def movey(self):
        '''
        The function makes the powerup moves along y-direction.
        '''
        if self.directiony == True:
            if self.point.y <= 1:
                self.directiony = False
                return self.point.y+self.speedy+1
            elif self.point.y <= self.speedy:
                return 1
            else:
                return self.point.y-self.speedy
        else:
            return self.point.y+self.speedy


    def automatic_move(self):
        '''
        Moves the power up on frame
        '''
        if self.display == False:
            return False

        new_y=self.movey()
        new_x=self.movex()
        
        if self.check_paddle_collision(new_x,new_y) or self.check_lost(new_y):
            self.remove_power_up()
            return False
        

        new_point = Point(new_x,new_y)      
        self.re_draw(new_point,self.shape,self.dimension)
        return True


    
    def gravity_effect(self):
        '''
        Will responsible for gravity effect n power ups.
        '''
        self.gtoc = time.time()
        if self.gtoc-self.gtic>self.gravityTP:
            self.gtic = self.gtoc
            if self.directiony:
                if (self.flag==3)and(self.speedy<=self.gravity):
                    self.directiony = False
                else:
                    self.flag += 1
            



    def self_move(self):
        '''
        The is function will automatically move powerup
        after certain time-interval
        '''
        self.power_up_start()
        self.gravity_effect()
        self.toc = time.time()
        if self.toc -self.tic >self.skip_iteration_tp:
            self.tic =self.toc
            self.automatic_move()
            if (self.active) and (self.toc - self.atic > self.active_time):
                self.active = False
                self.paddle.remove_cannon()
                for bullet in self.left_bullets:
                    bullet.remove_bullet()
                for bullet in self.right_bullets:
                    bullet.remove_bullet()
        else:
            pass


    
    def remove_power_up(self):
        '''
        Removes the powerup
        '''
        self.display = False
        self.shape = [[" "]]
        self.re_draw(self.point,self.shape,self.dimension)


    
    def lost_active_power_up(self):
        '''
        Method will lost all the active power up
        if a life is lost.
        '''
        self.active = False