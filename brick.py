from frame import Frame
from constants import BRICKHEIGHT, BRICKWIDTH, Dimension, Point
from colorama import Fore,Back,Style


class SingleBrick:
    '''
    class for single brick
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor of a single brick
        '''
        self.point = point
        self.dimension = Dimension(BRICKWIDTH,BRICKHEIGHT)
        self.shape = self.initial_shape()
        self.frame = frame




    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        return [
            [f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}"],
            [f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.WHITE}{Style.BRIGHT} {Style.RESET_ALL}"]
        ]
    
    def make_brick():
        '''
        '''



    def draw(self):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)



    def re_draw(self,new_point,new_shape,new_dimension):
        '''
        Re-render ball on the base Frame Paddle
        '''
        self.frame.restore_frame(new_point,new_shape,new_dimension,self.point,self.shape,self.dimension)
        self.point = new_point
        self.shape = new_shape
        self.dimension = new_dimension



class OneUnitBrick(SingleBrick):
    '''
    Bricks that will get destoyed on colliding once with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.draw()



class TwoUnitBrick(OneUnitBrick):
    '''
    Bricks that will get destoyed on colliding twice with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick with strength two unit
        '''
        return [
            [f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}"],
            [f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}"]
        ]



class ThreeUnitBrick(TwoUnitBrick):
    '''
    Bricks that will get destoyed on colliding thrice with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        return [
            [f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}"],
            [f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}"]
        ]



class UnbreakableBrick(SingleBrick):
    '''
    Bricks that are unbreakable but only get destroyed when collide with thru-ball
    or come together with ExplodingBrick (i.e. adjacent to them)
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        return [
            [f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}"],
            [f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.BLACK}{Style.BRIGHT} {Style.RESET_ALL}"]
        ]



class ExplodingBrick(SingleBrick):
    '''
    Special type of bricks that inhibits chain reaction.
    On colliding with ball it gets destroys along with
    other that are adjacent to it.
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        return [
            [f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"],
            [f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}",f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"]
        ]