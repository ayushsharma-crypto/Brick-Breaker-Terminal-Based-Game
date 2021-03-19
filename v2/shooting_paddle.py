from brick import BRICK_TYPE_ARRAY
from math import fabs
import time
from constants import Dimension, Point, SHOOTINGPADDLEACTIVETIME
from powerup import PowerUp
from colorama import *

class Bullet():
    '''
    class for bullets
    '''
    def __init__(self,frame,point):
        self.frame = frame
        self.point = Point(point.x,point.y)
        self.dimension = Dimension(1,1)
        self.shape = [[f"{Fore.GREEN}{Style.BRIGHT}|{Style.RESET_ALL}"]]
        self.used = False
        self.draw()
    


    def draw(self):
        '''
        Render bullet on the base Frame
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)
    


    def movey(self):
        '''
        Moving the bullet
        '''
        if self.used==True:
            return
        no = self.frame.current_frame[self.point.y-1][self.point.x]
        if (self.point.y<=1) or (no in BRICK_TYPE_ARRAY):
            # print("Striked")
            # time.sleep(2)
            # @TODO: Break Brick
            self.frame.clear_frame_area(self.point,self.dimension)
            self.used = True
        else:
            npoint = Point(self.point.x,self.point.y-1)
            self.frame.restore_frame(npoint,self.shape,self.dimension,self.point,self.shape,self.dimension)
            self.point = Point(self.point.x,self.point.y-1)


    
    def remove_bullet(self):
        '''
        remove bullect from screen
        '''
        self.frame.clear_frame_area(self.point,self.dimension)
        self.used = True





class ShootingPaddle(PowerUp):
    '''
    This is the class for shooting paddle power up.
    '''
    def __init__(self,ball,frame,paddle):
        '''
        constructor for this child class
        '''
        super().__init__(ball,frame,paddle,SHOOTINGPADDLEACTIVETIME)
        self.shoot_tic = time.time()
        self.timeinterval = 0.5
        self.left_bullets = []
        self.right_bullets = []
    


    def get_remain_time(self):
        '''
        returns the remaining time of the active power up
        '''
        if self.active:
            return int(self.active_time-int(time.time()-self.atic))


    def power_up_start(self):
        '''
        All effect will occur in this function.
        '''

        if self.active:

            all_active_index = []
            count = 0
            for i in range(len(self.ball.powerup)):
                if (self.ball.powerup[i].shape[0][0] == self.shape[0][0]) and self.ball.powerup[i].active:
                    all_active_index.append(i)
                    count += 1

            already = time.time()
            already_i = 1000
            for i in all_active_index:
                if self.ball.powerup[i].atic < already:
                    already = self.ball.powerup[i].atic
                    already_i = i
            
            for i in all_active_index:
                if i!=already_i:
                    self.ball.powerup[i].active = False
                    self.ball.powerup[already_i].active_time += SHOOTINGPADDLEACTIVETIME
            
            self.paddle.add_cannon()
            self.shoot_bullets()

            for bullet in self.left_bullets:
                bullet.movey()
            
            for bullet  in self.right_bullets:
                bullet.movey()

        
            print("Shooting Paddle Remaining Time = ",self.get_remain_time())
        return



    def shoot_bullets(self):
        '''
        Shooting the bullet after time-interval
        '''
        x= time.time()
        if x - self.shoot_tic > self.timeinterval:
            self.shoot_tic = x
            self.left_bullets.append(Bullet(self.frame,Point(self.paddle.point.x,self.paddle.point.y-1)))
            self.right_bullets.append(Bullet(self.frame,Point(self.paddle.point.x+self.paddle.dimension.width,self.paddle.point.y-1)))