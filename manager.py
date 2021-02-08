from frame import Frame

class Manager:
    def __init__(self, game_status):
        '''
        construct the walls, paddle, ball and frame
        '''
        self.game_status = game_status
        self.frame = Frame(self.game_status)
        self.frame.display()
        while True:
            self.schedular()
    
    def schedular(self):
        '''
        Order of execution at each iteration.
        ''' 