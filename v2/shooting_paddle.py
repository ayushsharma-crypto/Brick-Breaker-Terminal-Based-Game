import time
from constants import SHOOTINGPADDLEACTIVETIME
from powerup import PowerUp


class ShootingPaddle(PowerUp):
    '''
    This is the class for shooting paddle power up.
    '''
    def __init__(self,ball,frame,paddle):
        '''
        constructor for this child class
        '''
        super().__init__(ball,frame,paddle,SHOOTINGPADDLEACTIVETIME)
    


    def get_remain_time(self):
        '''
        returns the remaining time of the active power up
        '''
        if self.active:
            print("completed time = ",int(time.time()-self.atic))
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

        
            print("remaining time = ",self.get_remain_time())
        return