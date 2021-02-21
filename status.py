from arts import show_result
from time import time
from manager import Manager
from constants import MAXLIFE, MAXSTAGE

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
        self._stage = 1
        self._begin_time = time()

    def add_kill(self):
        '''
        Increase number of time the player got killed
        '''
        self._kill += 1
        if self._kill == self._life:
            show_result(self.ret_status())
            self.start_game()
    
    def stage_up(self):
        '''
        Staging up the player
        '''
        self._stage += 1
        if self._stage > MAXSTAGE:
            show_result(self.ret_status())
            self.reset_status()
        self.start_game(1)
    
    def add_score(self,increment):
        '''
        Increases player score by value 'increment'
        '''
        self._score += increment

    def get_time(self): 
        '''
        Returns current time from the start of the Game.
        '''
        return int(time()-self._begin_time)

    def get_stage(self): 
        '''
        Returns current stage of the Game.
        '''
        return self._stage

    def get_score(self): 
        '''
        Returns score of the current Game.
        '''
        return self._score
    
    def reset_status(self):
        '''
        Reset the status of the players
        '''
        self._kill = 0
        self._score = 0
        self._stage = 1
        self._begin_time = time()

    def ret_status(self):
        '''
        Return status of the Game
        '''
        return {
            'SCORE':self._score,
            'LIVES':str(self._life-self._kill)+'/'+str(self._life),
            'TIME':self.get_time(),
            'STAGE':self._stage
        }

    # def print_status(self):
    #     '''
    #     Print status of the Game
    #     '''
    #     print(
    #         "\033[2;1H" + 
    #         Fore.WHITE + Back.BLUE + Style.BRIGHT + 
    #         ("    SCORE: " + 
    #         str(self._score) + 
    #         "    |    LIVES: " + 
    #         str(str(self._life-self._kill)+'/'+str(self._life)) + 
    #         "    |    TIME: " +
    #         str(self.get_time()) + 
    #         "    |    STAGE: " + 
    #         str(self._stage) +
    #         "    " )
    #         )
    #     print(Style.RESET_ALL)    
    
    def start_game(self,flag = 0):
        '''
        Game will get started for given status
        '''
        if flag==0:
            self.reset_status()
        _ = Manager(self)