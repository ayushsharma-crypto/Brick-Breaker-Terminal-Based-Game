from time import time
from constants import MAXLIFE

class Status:
    def __init__(self):
        '''
        Contructor for Game Initialization
        '''
        self._life = MAXLIFE
        self._kill = 0
        self._score = 0
        self._stage = 0
        self._time = 0
        self._begin_time = time()

    def get_curr_time(self):
        '''
        '''
        return int(time()-self._begin_time)
    
    def get_remain_life(self):
        '''
        '''
        return self._life-self._kill
    
    def print_status(self):
        '''
        Return status of the Game
        '''
        print(
            'Score:',self._score,
            'Lives:',str(self.get_remain_life())+'/'+str(self._life),
            'Time:',self.get_curr_time(),
            'Stage:',self._stage
        )
        # print('Level = ', self._level, "\tScore = ", self._score, '\t Coins = ', self._coins,
            #   '\t Lives = ', self._life, '\t Time = ', self._time, '\t Kills = ', self._kills)