from frame import Frame
from paddle import Paddle
from user import KBHit

class Manager:
    def __init__(self, game_status):
        '''
        construct the walls, paddle, ball and frame
        '''
        self.game_status = game_status
        self.frame = Frame(self.game_status)
        self.paddle = Paddle(self.frame)
        self.frame.display()
        while True:
            self.schedular()
    
    def schedular(self):
        '''
        Order of execution at each iteration.
        ''' 
        self.user_input()


    def user_input(self):
        '''
        Getting input from the user for paddle movement
        '''
        kb = KBHit()
        ch = kb.getinput()
        if ch == 'a' or ch == 'A':
            self.paddle.move_left()
        elif ch == 'd' or ch == 'D':
            self.paddle.move_right()
        elif ch == 'q' or ch =='Q':
            quit()