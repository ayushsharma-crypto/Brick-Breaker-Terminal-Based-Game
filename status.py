from time import time
from manager import Manager
from constants import MAXLIFE

class Status:
    def __init__(self):
        '''
        Contructor for Game Initialization.

        Player will have maximum life = MAXLIFE and will stage up
        once break all the brick in a given stage, with life same
        as when player stages up.

        Time will be continued when he started playing game for 
        the first time.
        '''
        self._life = MAXLIFE
        self._kill = 0
        self._score = 0
        self._stage = 0
        self._begin_time = time()

    def add_kill(self):
        '''
        Increase number of time the player got killed
        '''
        self._kill += 1
        if self._kill == self._life:
            self.reset_status()
            self.start_game()
    
    def stage_up(self):
        '''
        Staging up the player
        '''
        self._stage += 1
        self.start_game()
    
    def add_score(self,increment):
        '''
        Increases player score by value 'increment'
        '''
        self._score += increment

    def get_time(self): 
        '''
        Returns current time from the start of the Game.
        '''
        return time()-self._begin_time
    
    def reset_status(self):
        '''
        Reset the status of the players
        '''
        self._kill = 0
        self._score = 0
        self._stage = 0
        self._begin_time = time()

    def print_status(self):
        '''
        Print status of the Game
        '''
        print(
            'Score:',self._score,
            'Lives:',str(self._life-self._kill)+'/'+str(self._life),
            'Time:',self.get_time(),
            'Stage:',self._stage
        )
    
    def start_game(self):
        '''
        '''
        _ = Manager(self)