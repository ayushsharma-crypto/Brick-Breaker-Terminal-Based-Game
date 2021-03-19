import time
from colorama.ansi import Back, Fore, Style
from constants import BALLSTEPTP, Dimension, FRAMEHEIGHT, FRAMEWIDTH, PADDLEHEIGHT, POWERUPGRAVITY, POWERUPWIDTH, Point
from frame import Frame

POWER_UP_ARRAY = []

class PowerUp:
    '''
    A class for various power implementation.
    '''
    def __init__(self,ball,frame: Frame,paddle):
        self.ball = ball
        self.frame = frame
        self.point = ball.point
        self.paddle = paddle
        self.dimension = Dimension(POWERUPWIDTH,PADDLEHEIGHT)
        self.shape = self.shape_powerup()
        self.gravity = POWERUPGRAVITY
        self.speedx = ball.speedx
        self.speedy = ball.speedy
        self.directionx = ball.direction_x
        self.directiony = ball.direction_y
        self.display = True
        self.toc = time.time()
        self.tic = time.time()
        self.skip_iteration_tp = BALLSTEPTP
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
        Render ball on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension
            


    def check_paddle_collision(self,new_x,new_y):
        '''
        Checks if the ball was catched by the paddle.
        '''
        if self.frame.current_frame[new_y][new_x] == self.paddle.shape[0][0]:
            return True
            # @TODO : Work with powerup
        else:
            return False
            


    def check_lost(self,new_y):
        '''
        Checks if the ball was not catched by the paddle.
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
            # @TODO : Gravity effeect and paddle collision
            return self.point.y+self.speedy


    def automatic_move(self):
        '''
        Moves the power up on frame
        '''
        if self.display == False:
            return False

        new_y=self.movey()
        new_x=self.movex()

        # print("new_x = ",new_x," new_y = ",new_y)
        # time.sleep(2)
        
        if self.check_paddle_collision(new_x,new_y) or self.check_lost(new_y):
            self.remove_power_up()
            return False
        

        new_point = Point(new_x,new_y)      
        self.re_draw(new_point,self.shape,self.dimension)
        return True



    def self_move(self):
        '''
        The is function will automatically move powerup
        after certain time-interval
        '''
        self.toc = time.time()
        if self.toc -self.tic >self.skip_iteration_tp:
            self.tic =self.toc
            self.automatic_move()
        else:
            pass


    
    def remove_power_up(self):
        '''
        Removes the powerup
        '''
        self.display = False
        self.shape = [[" "]]
        self.re_draw(self.point,self.shape,self.dimension)